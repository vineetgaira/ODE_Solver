
"""This one's job is which algorithm to run ."""
from src.methods import euler, rk2, rk4

def solve(method, equation, x0, y0, h ):

    methods = {"euler": euler,
    "heun": rk2,
    "midpoint": rk2,
    "raltson": rk2,
    "rk4": rk4
}

def solve_with_method():
    pass

def compare_methods():
    pass