import numpy as np
import sympy as sym
from sympy import Interval
from sympy.utilities.lambdify import lambdify
from sympy.calculus.util import maximum

# Random shit
t = sym.symbols("t")

# Read input
func = sym.sympify(input())
points = int(input())
point_start, point_end = map(float, input().split())

# Do the sampling
sample_x = np.random.uniform(low=point_start, high=point_end, size=(points,))
# https://stackoverflow.com/a/10683911/4213397
lambdify_t = lambdify(t, func, 'numpy')
evaluated_y = lambdify_t(sample_x)
max_y = np.max(evaluated_y) # Look ma! Monte Carlo in Monte Carlo!
sample_y = np.random.uniform(low=0, high=np.max(evaluated_y), size=(points,))

# Count and finalize
below_graph = sample_y <= evaluated_y
print(np.round(below_graph.sum() * max_y * (point_end - point_start) / points, 2))