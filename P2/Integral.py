import numpy as np
import numpy.typing as npt
import sympy as sym
from sympy.utilities.lambdify import lambdify

# Random shit
x = sym.symbols("x")

# Read input
func = sym.sympify(input())
n = int(input())
point_start, point_end = map(float, input().split())
real_integral = sym.integrate(func, (x, point_start, point_end))
h = (point_end - point_start) / n
intervals_begins = np.linspace(point_start, point_end - h, num=n, dtype=np.float64)

# Define integration functions
def rectangle_method(intervals: npt.NDArray[np.float64]) -> float:
    lambdify_x = lambdify(x, func, 'numpy')
    evaluated_y = lambdify_x(intervals)
    return evaluated_y.sum() * h

def midpoint_method(intervals: npt.NDArray[np.float64]) -> float:
    intervals_fixed = intervals + (h / 2)
    lambdify_x = lambdify(x, func, 'numpy')
    evaluated_y = lambdify_x(intervals_fixed)
    return evaluated_y.sum() * h

def trapezoidal_method(intervals: npt.NDArray[np.float64]) -> float:
    intervals_fixed = np.append(intervals, [point_end])
    lambdify_x = lambdify(x, func, 'numpy')
    evaluated_y = lambdify_x(intervals_fixed)
    sum_of_y = evaluated_y[1:-1].sum() * 2
    sum_of_y += evaluated_y[0] + evaluated_y[-1]
    return sum_of_y * h / 2

def simpson_method(_: npt.NDArray[np.float64]) -> float:
    n_2 = n * 2 # Based on group chat
    h = (point_end - point_start) / n_2
    intervals_begins = np.linspace(point_start, point_end - h, num=n_2, dtype=np.float64)
    intervals_fixed = np.append(intervals_begins, [point_end])
    lambdify_x = lambdify(x, func, 'numpy')
    evaluated_y = lambdify_x(intervals_fixed)
    sum_of_y = evaluated_y[0] + evaluated_y[-1]
    sum_of_y += evaluated_y[1:-1][::2].sum() * 4
    sum_of_y += evaluated_y[1:-1][1::2].sum() * 2
    return sum_of_y * h / 3

def calculate_method(func):
    method_result = func(intervals_begins)
    print(f"{np.round(method_result, 3)} {np.round(np.abs(float(method_result - real_integral)), 3)}")

calculate_method(rectangle_method)
calculate_method(midpoint_method)
calculate_method(trapezoidal_method)
calculate_method(simpson_method)