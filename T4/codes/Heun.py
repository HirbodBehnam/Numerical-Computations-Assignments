ENDPOINTS = (0, 1)
N = 5
INITIAL_VALUE = 0
def my_function(x: float, y: float) -> float:
    return 1 / (1 + x * x) - 2 * y

h = (ENDPOINTS[1] - ENDPOINTS[0]) / N
print("h:", h)
t = ENDPOINTS[0]
w = INITIAL_VALUE
print(f"({t}, {w})")

for i in range(1, N + 1):
    k1 = h * my_function(t, w)
    k2 = h * my_function(t + 2*h/3, w + 2*k1/3)
    w = w + (k1 + 3*k2)/4
    t += h
    print(f"({k1}, {k2}) ({t}, {w})")