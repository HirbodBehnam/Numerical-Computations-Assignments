import numpy as np
import sympy as sym
import math

# Random shit
x, y = sym.symbols("x y")

# Read input
func = sym.sympify(input())
base_x, base_y = map(float, input().split())
to_estimate_x, to_estimate_y = map(float, input().split())
iterations = int(input())

# Calculate each poly
result = 0
for nth_poly in range(iterations+1):
    current_result = 0
    x_diffs = nth_poly
    y_diffs = 0
    # The polys inside the 1/n!
    for _ in range(nth_poly + 1):
        temp_function = func
        for _ in range(x_diffs):
            temp_function = temp_function.diff(x)
        for _ in range(y_diffs):
            temp_function = temp_function.diff(y)
        current_result += temp_function.subs(x, base_x).subs(y, base_y) * ((to_estimate_x - base_x) ** x_diffs) * ((to_estimate_y - base_y) ** y_diffs) * math.comb(nth_poly, x_diffs)
        x_diffs -= 1
        y_diffs += 1
    result += current_result / math.factorial(nth_poly)

# The results
print(np.round(float(result), 4))
print(np.round(float(func.subs(x, to_estimate_x).subs(y, to_estimate_y)), 4))