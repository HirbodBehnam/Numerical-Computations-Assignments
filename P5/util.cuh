#ifndef P5_UTIL_CUH
#define P5_UTIL_CUH

/***
 * Sums all elements on a device array
 * @param device_mem The array on device
 * @param size Size of array
 * @return Sum of all elements
 */
float reduce_sum(float *device_mem, unsigned int size);

#endif //P5_UTIL_CUH
