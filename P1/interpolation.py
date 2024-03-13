import numpy as np
import sympy as sym

# Random shit
x = sym.Symbol("x")

# Read input
func = sym.sympify(input())
points = list(map(float, input().split()))
target_x = float(input())

# Lagrange interpolation
estimate_of_func_lagrange = 0
for term in points:
    result = 1
    for zero_term in points:
        if zero_term == term:
            continue
        result *= (target_x - zero_term) / (term - zero_term)
    print(np.round(result, 3), end=" ")
    estimate_of_func_lagrange += result * float(func.subs(x, term))
print()

# Newton interpolation
current_term = list(map(lambda point_x: float(func.subs(x, point_x)), points))
estimate_of_func_newton = current_term[0]
print(np.round(current_term[0], 3), end=" ")
iteration = 1
# https://youtu.be/S7QIU0i1qLE?si=jahESeYAld055zob&t=656
while len(current_term) != 1:
    temporary_terms = []
    for i in range(len(current_term) - 1):
        next_number = (current_term[i + 1] - current_term[i]) / (points[i + iteration] - points[i])
        temporary_terms.append(next_number)
    current_term = temporary_terms
    print(np.round(current_term[0], 3), end=" ")
    current_estimate_term = current_term[0]
    for i in range(iteration):
        current_estimate_term *= target_x - points[i]
    estimate_of_func_newton += current_estimate_term
    iteration += 1

print()
print(np.round(estimate_of_func_lagrange, 3))