import numpy as np

L_INV = np.array([[0.04, 0, 0], [-0.32, 0.125, 0], [-1.92, -1.5, 1]])
U = np.array([[0, 5, 1], [0, 0, 1], [0, 0, 0]])
B = np.array([106.8, 177.2, 279.2])
x = np.array([1,2,5])

for _ in range(10):
    x = L_INV @ (B - (U @ x))
    print(x)