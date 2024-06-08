import numpy as np

def fucked_up():
    A = [
        [4, -1, 0],
        [-1, 4, -1],
        [0, -1, 4],
    ]
    B = [3, 2, 3]
    x = [0, 0, 0]
    for _ in range(5):
        next_x = [0] * len(x)
        for i in range(len(next_x)):
            result = B[i]
            for j in range(len(x)):
                if i == j:
                    continue
                result -= A[i][j] * x[j]
            x[i] = result / A[i][i]
        print(x)

def matrix_based():
    B = np.array([3, 2, 3])
    D_INV = np.diag([0.25, 0.25, 0.25])
    LU = np.array([
        [0, -1, 0],
        [-1, 0, -1],
        [0, -1, 0],
    ])
    x = np.zeros(3)
    for _ in range(5):
        x = D_INV @ (B - (LU @ x))
        print(x)

fucked_up()
print()
matrix_based()