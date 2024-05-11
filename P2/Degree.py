import numpy as np
import sympy as sym

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

terms = sym.Poly(sym.expand(sym.simplify(generate_lagrange_poly()))).all_coeffs()
for degree, term in enumerate(terms):
    if term < 10e-6:
        continue
    print(len(terms) - degree - 1)
    exit()