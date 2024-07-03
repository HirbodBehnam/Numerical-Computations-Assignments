#include <iostream>
#include "q4.cuh"

int main() {
    float xs[] = {1, 2, 3, 4, 5, 6, 7};
    float fxs[] = {2, 3, 5, 7, 10, 4, 10};
    std::cout << integrate(1, 7, xs, fxs, 7) << std::endl;
    return 0;
}
