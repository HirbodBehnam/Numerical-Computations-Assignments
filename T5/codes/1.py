def f(x: float) -> float:
    return (2 * x * x - 1) / (4 * (x - 1))

def fixed_point(start: float):
    x = 0
    for i in range(10):
        next_x = f(x)
        print(f"x_{{{i}}} = f({x}) &= {next_x}\\\\")
        x = next_x

fixed_point(0)