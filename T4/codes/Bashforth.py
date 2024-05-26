ENDPOINTS = (0, 20)
h = 0.5
INITIAL_VALUE = 6
def my_function(x: float, y: float) -> float:
    return 0.2 * y - 0.1 * y * y
# Use euler method
INITIAL_VALUE_2 = INITIAL_VALUE + h * my_function(ENDPOINTS[0], INITIAL_VALUE)

current_values: list[float] = [INITIAL_VALUE, INITIAL_VALUE_2]
current_t: list[float] = [ENDPOINTS[0], ENDPOINTS[0] + h]
while current_t[-1] < ENDPOINTS[1]:
    current_values.append(current_t[-1] + 3/2*h*my_function(current_t[-1], current_values[-1]) + h*my_function(current_t[-2], current_values[-2])/2)
    current_t.append(current_t[-1] + h)
print(current_values)
print(current_t)