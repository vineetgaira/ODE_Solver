"This file stores all the solver methods."

from src.parser import parse_equation


def euler(x, y, h, equation):

    return y + h(equation)

def modified_euler(x, y):
    pass

def midpoint(x, y):
    pass

def rk2(x, y):
    pass

def rk4(x, y):
    pass