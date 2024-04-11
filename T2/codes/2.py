import numpy as np

def P(x: int):
    return np.array([x ** i for i in range(5)], dtype=np.int64)

def delta_P(delta: int, x: int):
    if delta == 0:
        return P(x)
    if delta == 1:
        return P(x + 1) - P(x)
    return delta_P(delta - 1, x + 1) - delta_P(delta - 1, x)

TO = 4
for i in range(TO + 1):
    for j in range(i + 1):
        print(f"\\Delta^{TO - i} P({j}) = {delta_P(TO - i, j)}")

print(delta_P(2, 10))
print(P(12) - 2 * P(11) + P(10))
