import numpy as np
from numpy.linalg import inv

degree_of_result = int(input())
number_of_points = int(input())
points = [list(map(float, input().split())) for _ in range(number_of_points)]
x_values = list(map(lambda p: p[0], points))
y_values = list(map(lambda p: p[1], points))

X = np.array([[x ** i for i in range(degree_of_result + 1)] for x in x_values])
result = np.round((inv(X.T @ X) @ X.T) @ np.array(y_values), 2)
for b in result[::-1]:
    print("{:.2f}".format(b), end=" ")
