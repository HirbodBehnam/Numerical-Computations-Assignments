__global__ void five_point(const float *y_terms, float *result, float h) {
    unsigned int size = blockDim.x;
    unsigned int i = threadIdx.x;
    if (i < 2 || i >= size - 2) {
        return;
    }
    result[i] = (y_terms[i - 2] - 8 * y_terms[i - 1] + 8 * y_terms[i + 1] - y_terms[i + 2]) / (12 * h);
}

void differentiate(float *xs, float *fxs, int length, float *out) {
    // Move everything to cuda memory
    float *fxs_gpu, *result;
    cudaMalloc(&fxs_gpu, sizeof(float) * length);
    cudaMemcpy(fxs_gpu, fxs, sizeof(float) * length, cudaMemcpyHostToDevice);
    cudaMalloc(&result, sizeof(float) * length);
    // Calculate the points
    five_point<<<1, length>>>(fxs_gpu, result, xs[1] - xs[0]);
    cudaMemcpy(out, result, sizeof(float) * length, cudaMemcpyDeviceToHost);
    // Clean up
    cudaFree(fxs_gpu);
    cudaFree(result);
}