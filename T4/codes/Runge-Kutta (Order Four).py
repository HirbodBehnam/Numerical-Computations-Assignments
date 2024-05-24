import math

ENDPOINTS = (1, 1.3)
N = 3
INITIAL_VALUE = 1
def my_function(x: float, y: float) -> float:
    return x * math.pow(y, 1/3)

h = (ENDPOINTS[1] - ENDPOINTS[0]) / N
print("h:", h)
t = ENDPOINTS[0]
w = INITIAL_VALUE
print(f"({t}, {w})")

for i in range(1, N + 1):
    k1 = h * my_function(t, w)
    k2 = h * my_function(t + h/2, w + k1/2)
    k3 = h * my_function(t + h/2, w + k1/2)
    k4 = h * my_function(t + h, w + k3)
    w = w + (k1 + 2*k2 + 2*k3 + k4)/6
    t += h
    print(f"({t}, {w})")