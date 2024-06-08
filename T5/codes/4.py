import math

def f(x: float) -> float:
    return 10 ** x - 56

def diff_f(x: float) -> float:
    return 10 ** x * math.log(10)

def fixed_point(start: float) -> float:
    x = start
    a = 0.01
    print(f"a_{{0}} &= {x}")
    for i in range(10):
        next_x = x - a * f(x)
        print(f"a_{{{i + 1}}} = {x} - {a} \\times f({x}) &= {next_x}")
        x = next_x

def newton_raphson(start: float) -> float:
    x = start
    print(f"a_{{0}} &= {x}")
    for i in range(10):
        next_x = x - f(x) / diff_f(x)
        print(f"a_{{{i + 1}}} = {x} - \\frac{{f({x})}}{{f'({x})}} &= {next_x}")
        x = next_x

fixed_point(1)
newton_raphson(1)