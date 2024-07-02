cmake_minimum_required(VERSION 3.28)
project(P5 CUDA)

set(CMAKE_CUDA_STANDARD 17)

add_executable(P5 main.cu
        q1.cuh
        q1.cu
        q2.cuh
        q2.cu
        util.cuh
        util.cu
        q3.cuh
        q3.cu
        q4.cuh
        q4.cu
)

set_target_properties(P5 PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON
        CUDA_ARCHITECTURES all)
