
"""This one's job is which algorithm to run ."""
from src.methods import euler, rk2, rk4

def solve(method, equation, x0, y0, h ):

    methods = {"euler": euler(equation, x0, y0, h),
    "heun": rk2(equation, x0, y0, h, alpha = 1, beta = 1, c1 = 1/2, c2 = 1/2),
    "midpoint": rk2(equation, x0, y0, h, alpha = 1/2, beta = 1/2, c1 = 0, c2 = 1),
    "raltson": rk2(equation, x0, y0, h, alpha = 2/3, beta = 2/3, c1 = 1/4, c2 = 3/4),
    "rk4": rk4(equation, x0, y0, h)
}

def solve_with_method():
    pass

def compare_methods():
    pass