#include <iostream>
#include "util.cuh"

__global__ void calculate_terms(float *coefficients, float x) {
    unsigned int tid = threadIdx.x;
    coefficients[tid] *= powf(x, static_cast<float>(tid));
}

float calculatePolynomial(const float *coefficients, int length, float x) {
    // Move everything to cuda memory
    float *coefficients_gpu;
    cudaMalloc(&coefficients_gpu, sizeof(float) * length);
    cudaMemcpy(coefficients_gpu, coefficients, sizeof(float) * length, cudaMemcpyHostToDevice);
    // Calculate the terms
    calculate_terms<<<1, length>>>(coefficients_gpu, x);
    float result = reduce_sum(coefficients_gpu, length);
    cudaFree(coefficients_gpu);
    return result;
}