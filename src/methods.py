"This file stores all the solver methods."\

from src.parser import f

def euler(equation, x0, y0, h):
    slope = f(equation, x0, y0)
    x1 = x0 + h
    y1 = y0 + h * slope
    return x1, y1

def modified_euler(equation, x0, y0, y_1_o, h):
    x_one = x0 + h
    f1 = f(equation, x0, y0)
    f2 =  f(equation, x_one, y_1_o)
    y_1_1 = y0 + h/2*( f1 + f2)

    return x_one, y_1_1

def midpoint(x, y):
    pass

def rk2(x, y):
    pass

def rk4(x, y):
    pass