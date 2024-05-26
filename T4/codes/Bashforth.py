ENDPOINTS = (0, 20)
h = 2
INITIAL_VALUE = 6
def my_function(x: float, y: float) -> float:
    return 0.2 * y - 0.1 * y * y
# Use euler method
INITIAL_VALUE_2 = INITIAL_VALUE + h * my_function(ENDPOINTS[0], INITIAL_VALUE)

current_values: list[float] = [INITIAL_VALUE, INITIAL_VALUE_2]
current_t: list[float] = [ENDPOINTS[0], ENDPOINTS[0] + h]
while current_t[-1] < ENDPOINTS[1]:
    current_values.append(current_values[-1] + 3/2*h*my_function(current_t[-1], current_values[-1]) - h*my_function(current_t[-2], current_values[-2])/2)
    current_t.append(current_t[-1] + h)
print(current_values)
print(current_t)

# Latex
for i in range(1, len(current_values)):
    print(f"y_{i + 1} &= y_{i} + \\frac{{3}}{{2}} \\times {h} (0.2 \\times {current_values[i]:.4f} - 0.1 \\times {current_values[i]:.4f}) - \\frac{{{h}}}{{2}} (0.2 \\times {current_values[i - 1]:.4f} - 0.1 \\times {current_values[i - 1]:.4f}) = {current_values[i]:.4}\\\\")