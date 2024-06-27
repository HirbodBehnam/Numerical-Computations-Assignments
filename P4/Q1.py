import numpy as np
import numpy.linalg as alg

# Get the equations
number_of_equations = int(input())
equations = np.array([list(map(float, input().split())) for _ in range(number_of_equations)])
b = equations[:, -1]
equations = equations[:, :-1]
equations_det = alg.det(equations)

# Replace each column
for i in range(number_of_equations):
    copied_equations = equations.copy()
    copied_equations[:, i] = b
    print("{:.2f}".format(np.round(alg.det(copied_equations) / equations_det, 2)), end=" ")