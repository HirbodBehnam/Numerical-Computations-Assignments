import numpy as np
import sympy as sym
import math

# Random shit
x = sym.Symbol("x")

# Read input
func = sym.sympify(input())
a, b = list(map(float, input().split()))
target_x = float(input())
point_count = int(input())

# Chebyshev Points
chebyshev_points = list(
    map(
        lambda k: (
            a + b + (b - a) * math.cos((2 * k - 1) * math.pi / (2 * point_count))
        )
        / 2,
        range(1, point_count + 1),
    ),
)

# Uniform points
uniform_points = list(
    map(
        lambda k: a + (b - a) * (k - 1) / (point_count - 1),
        range(1, point_count + 1),
    ),
)

def newton_interpolation(points) -> float:
    current_term = list(map(lambda point_x: float(func.subs(x, point_x)), points))
    estimate_of_func_newton = current_term[0]
    iteration = 1
    # https://youtu.be/S7QIU0i1qLE?si=jahESeYAld055zob&t=656
    while len(current_term) != 1:
        temporary_terms = []
        for i in range(len(current_term) - 1):
            next_number = (current_term[i + 1] - current_term[i]) / (points[i + iteration] - points[i])
            temporary_terms.append(next_number)
        current_term = temporary_terms
        current_estimate_term = current_term[0]
        for i in range(iteration):
            current_estimate_term *= target_x - points[i]
        estimate_of_func_newton += current_estimate_term
        iteration += 1
    
    return estimate_of_func_newton

chebyshev_estimation = newton_interpolation(chebyshev_points)
uniform_estimation = newton_interpolation(uniform_points)
print(np.round(chebyshev_estimation, 3))
print(np.round(uniform_estimation, 3))
print(np.abs(np.round(uniform_estimation - chebyshev_estimation, 3)))