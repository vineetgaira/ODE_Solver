"This file stores all the solver methods."\

from src.parser import f

def euler(equation, x0, y0, h):
    slope = f(equation, x0, y0)
    x1 = x0 + h
    y1 = y0 + h * slope
    return x1, y1

def modified_euler(y0, h, euler_value, ):

    return y0 + h[euler_value, ]
   

def midpoint(x, y):
    pass

def rk2(x, y):
    pass

def rk4(x, y):
    pass