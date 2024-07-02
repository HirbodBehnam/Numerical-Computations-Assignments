#define REDUCTION_OUTPUT_SIZE 1

__global__ void reduce_sum_device(const float *g_idata, float *g_odata) {
    extern __shared__ float sdata[];
    // each thread loads one element from global to shared mem
    unsigned int tid = threadIdx.x;
    unsigned int i = blockIdx.x * (blockDim.x * 2) + threadIdx.x;
    sdata[tid] = g_idata[i] + g_idata[i + blockDim.x];
    __syncthreads();

    // do reduction in shared mem
    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] += sdata[tid + s];
        }
        __syncthreads();
    }
    // write result for this block to global mem
    if (tid == 0)
        g_odata[blockIdx.x] = sdata[0];
}

/***
 * Finds the next power of two of a number.
 * https://stackoverflow.com/a/2681094
 * @param x The number to find its next power of two.
 * @return The next power of two.
 */
unsigned int prev_power_of_two(unsigned int x) {
    x = x | (x >> 1);
    x = x | (x >> 2);
    x = x | (x >> 4);
    x = x | (x >> 8);
    x = x | (x >> 16);
    return x - (x >> 1);
}

float reduce_sum(float *device_mem, unsigned int size) {
    // Find the previous power of two
    unsigned int power_of_two_size = prev_power_of_two(size);
    float *output_reduction;
    cudaMalloc(&output_reduction, sizeof(float) * REDUCTION_OUTPUT_SIZE);
    // Reduce
    reduce_sum_device<<<REDUCTION_OUTPUT_SIZE, power_of_two_size / REDUCTION_OUTPUT_SIZE, power_of_two_size / REDUCTION_OUTPUT_SIZE>>>(device_mem,
                                                                                                      output_reduction);
    // Move back result to CPU
    float reduction_result[REDUCTION_OUTPUT_SIZE];
    cudaMemcpy(reduction_result, output_reduction, sizeof(float) * REDUCTION_OUTPUT_SIZE, cudaMemcpyDeviceToHost);
    cudaFree(output_reduction);
    // Final reduction on CPU
    float result = 0;
    for (float i: reduction_result)
        result += i;
    // Also the rest of array
    unsigned int rest_size = size - power_of_two_size;
    auto *rest_of_array = new float[rest_size];
    cudaMemcpy(rest_of_array, device_mem + power_of_two_size, sizeof(float) * rest_size, cudaMemcpyDeviceToHost);
    for (unsigned int i = 0; i < rest_size; i++) {
        result += rest_of_array[i];
    }
    delete[] rest_of_array;
    cudaFree(output_reduction);
    return result;
}