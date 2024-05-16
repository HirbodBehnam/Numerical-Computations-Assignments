import numpy as np
import sympy as sym
from sympy.utilities.lambdify import lambdify

# Random shit
x = sym.symbols("x")

# Read input
input() # We dont care about the count of the numbers
points = list(zip(map(float, input().split()), map(float, input().split())))

# Create the lagrange polynomial
def generate_term(n: int):
    result = points[n][1]
    for i in range(len(points)):
        if i == n:
            continue
        result *= (x - points[i][0]) / (points[n][0] - points[i][0])
    return result

def generate_lagrange_poly():
    lagrange_poly = 0
    for i in range(len(points)):
        lagrange_poly += generate_term(i)
    return lagrange_poly

degree = 0
try:
    while True:
        lambdify_x = lambdify(x, sym.diff(generate_lagrange_poly(), x), 'numpy')
        new_point_y = lambdify_x(np.array(list(map(lambda x: x[0], points))))
        if all(map(lambda x: x < 10e-6, new_point_y)):
            print(degree)
            break
        # Fix points
        points = list(filter(lambda x: x[1] > 10e-6, zip(map(lambda x: x[0], points), list(new_point_y))))
        degree += 1
except: # Not sure when we reach here
    pass