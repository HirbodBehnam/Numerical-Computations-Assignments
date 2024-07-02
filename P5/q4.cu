#include "util.cuh"

__global__ void simpson_13_method(const float *y_terms, float *result) {
    unsigned int size = blockDim.x;
    unsigned int i = threadIdx.x;
    if (threadIdx.x == 0 || threadIdx.x == size - 1) {
        result[i] = y_terms[i];
    } else if (i % 2 == 1) {
        result[i] = 4 * y_terms[i];
    } else {
        result[i] = 2 * y_terms[i];
    }
}

float integrate(float start, float end, float *xs, float *fxs, int length) {
    // Move everything to cuda memory
    float *fxs_gpu, *simpson_array;
    cudaMalloc(&fxs_gpu, sizeof(float) * length);
    cudaMemcpy(fxs_gpu, fxs, sizeof(float) * length, cudaMemcpyHostToDevice);
    cudaMalloc(&simpson_array, sizeof(float) * length);
    float h = xs[1] - xs[0];
    // Do the calculations
    simpson_13_method<<<1, length>>>(fxs_gpu, simpson_array);
    float result = reduce_sum(simpson_array, length);
    // Cleanup
    cudaFree(fxs_gpu);
    cudaFree(simpson_array);
    return h * result / 3;
}
