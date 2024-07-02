#include <iostream>
#include "q1.cuh"

int main() {
    float coefficients[] = {1, -2, 1};
    std::cout << calculatePolynomial(coefficients, 4, 10);
    return 0;
}
