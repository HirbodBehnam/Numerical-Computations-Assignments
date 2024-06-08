def f(x: float) -> float:
    return x * x * x - 13 * x * x + 76

def secant_method(x0: float, x1: float) -> float:
    print(f"p_0 &= {x0}\\\\")
    print(f"p_1 &= {x1}\\\\")
    for i in range(10):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"p_{{{i+2}}} = {x1} - \\frac{{f({x1}) ({x1} - {x0})}}{{f({x1}) - f({x0})}} &= {x2}\\\\")
        x0, x1 = x1, x2
        if abs(f(x2)) < 0.01:
            return x2
    return x2

def bisection(a: float, b: float) -> float:
    while True:
        p = (a + b) / 2
        print(f"a = {a} & b = {b} & p = \\frac{{{a} + {b}}}{{2}} = {p}\\\\")
        if abs(f(p)) < 0.01:
            break
        if (f(p) > 0 and f(a) > 0) or (f(p) < 0 and f(a) < 0):
            a = p
        else:
            b = p
    return p

secant_method(2, 3)
bisection(2, 3)