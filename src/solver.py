
"""This one's job is which algorithm to run ."""
from src.methods import euler, heun, midpoint, ralston, rk4

METHODS_REGISTRY= {"euler": euler,
    "heun": heun,
    "midpoint": midpoint,
    "raltson": ralston,
    "rk4": rk4
}

def solve_with_method(method_name, equation, x0, y0, target_x, h):
    method_fn = METHODS_REGISTRY[method_name]
    history = [(x0, y0)]
    n_steps = round((target_x - x0)/h)
    for i in range(n_steps):
        x0, y0 = method_fn(equation, x0, y0, h)
        history.append((round(x0, 5), round(y0, 5)))
    return history
    
def compare_methods(equation, x0, y0, target_x, h):
    return {
        name :solve_with_method(name, equation, x0, y0, target_x, h)
        for name in METHODS_REGISTRY
    }
