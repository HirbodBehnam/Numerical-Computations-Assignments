import numpy as np

POINTS = [(-1, 0.5), (0, 1), (1, 2), (2, 4)]

h = [POINTS[i + 1][0] - POINTS[i][0] for i in range(len(POINTS) - 1)]
print("h:", h)

a = [POINTS[i][1] for i in range(len(POINTS))]
print("a:", a)

a_matrix = np.zeros((len(POINTS), len(POINTS)), dtype=np.float64)
a_matrix[0, 0] = 1
a_matrix[-1, -1] = 1
for i in range(len(h)-1):
    a_matrix[i + 1, i] = h[i]
    a_matrix[i + 1, i+1] = 2*(h[i] + h[i+1])
    a_matrix[i + 1, i+2] = h[i + 1]
print("A:\n", a_matrix)

b_vector = np.zeros(len(POINTS), dtype=np.float64)
for i in range(len(h)-1):
    b_vector[i+1] = 3 / h[i+1] * (a[i+2] - a[i+1]) - 3 / h[i] * (a[i+1] - a[i])
print("b vector:", b_vector)

c = np.linalg.solve(a_matrix, b_vector)
print("c:", c)
#print(a_matrix @ c)

b = np.zeros(len(POINTS) - 1, dtype=np.float64)
d = np.zeros(len(POINTS) - 1, dtype=np.float64)
for i in range(len(POINTS) - 1):
    b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
    d[i] = (c[i + 1] - c[i]) / (3 * h[i])
print("b:", b)
print("d:", d)