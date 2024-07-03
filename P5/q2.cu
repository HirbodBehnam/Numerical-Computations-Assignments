#include "util.cuh"
#include <stdio.h>

__global__ void calculate_l_terms(const float *x_terms, float *l_terms, float x) {
    unsigned int j = threadIdx.x;
    unsigned int k = blockDim.x;
    float result = 1;
    for (unsigned int m = 0; m < k; m++) {
        if (m == j)
            continue;
        result *= (x - x_terms[m]) / (x_terms[j] - x_terms[m]);
    }
    l_terms[j] = result;
}

__global__ void calculate_ly_terms(const float *y_terms, float *l_terms) {
    unsigned int i = threadIdx.x;
    l_terms[i] *= y_terms[i];
}

__global__ void divided_differences(const float *x_terms, const float *y_terms, float *result, float x) {
    extern __shared__ float prev_data[];
    extern __shared__ float current_data[];
    unsigned int i = threadIdx.x;
    prev_data[i] = y_terms[i];
    __syncthreads();

    for (unsigned int j = 0; j < i; j++) {
        current_data[i] = (prev_data[i] - prev_data[i - 1]) / (x_terms[i]- x_terms[i - j - 1]);
        __syncthreads();
        prev_data[i] = current_data[i];
        __syncthreads();
    }

    result[i] = prev_data[i];
    for (unsigned int j = 0; j < i; j++) {
        result[i] *= (x - x_terms[j]);
    }
}

float lagrangeInterpolate(float *xs, float *fxs, int length, float x) {
    // Move everything to cuda memory
    float *xs_gpu, *fxs_gpu, *l_terms;
    cudaMalloc(&xs_gpu, sizeof(float) * length);
    cudaMemcpy(xs_gpu, xs, sizeof(float) * length, cudaMemcpyHostToDevice);
    cudaMalloc(&fxs_gpu, sizeof(float) * length);
    cudaMemcpy(fxs_gpu, fxs, sizeof(float) * length, cudaMemcpyHostToDevice);
    cudaMalloc(&l_terms, sizeof(float) * length);
    // Calculate the terms
    calculate_l_terms<<<1, length>>>(xs_gpu, l_terms, x);
    calculate_ly_terms<<<1, length>>>(fxs_gpu, l_terms);
    float result = reduce_sum(l_terms, length);
    // Cleanup
    cudaFree(xs_gpu);
    cudaFree(fxs_gpu);
    cudaFree(l_terms);
    return result;
}

float newtonInterpolate(float *xs, float *fxs, int length, float x) {
    // Move everything to cuda memory
    float *xs_gpu, *fxs_gpu, *divided_differences_terms;
    cudaMalloc(&xs_gpu, sizeof(float) * length);
    cudaMemcpy(xs_gpu, xs, sizeof(float) * length, cudaMemcpyHostToDevice);
    cudaMalloc(&fxs_gpu, sizeof(float) * length);
    cudaMemcpy(fxs_gpu, fxs, sizeof(float) * length, cudaMemcpyHostToDevice);
    cudaMalloc(&divided_differences_terms, sizeof(float) * length);
    // Calculate terms
    divided_differences<<<1, length, length>>>(xs_gpu, fxs_gpu, divided_differences_terms, x);
    float result = reduce_sum(divided_differences_terms, length);
    // Cleanup
    cudaFree(xs_gpu);
    cudaFree(fxs_gpu);
    cudaFree(divided_differences_terms);
    return result;
}