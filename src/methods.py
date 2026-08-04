"This file stores all the solver methods."\

from src.parser import f

def euler(equation, x0, y0, h):
    slope = f(equation, x0, y0)
    x1 = x0 + h
    y1 = y0 + h * slope
    return x1, y1

def rk2(equation, x0, y0, h, alpha, beta, c1, c2):

    x1 = x0 + h
    
    k1 = f(equation, x0, y0)
    k2 = f(equation, x0 + alpha*h, y0 + beta*h*k1)

    y1 = y0 + h*(c1*k1 + c2*k2)

    return x1, y1

def heun(equation, x0, y0, h):
   
   return rk2(equation, x0, y0, h, alpha = 1, beta = 1, c1 = 1/2, c2 = 1/2)

def midpoint(equation, x0, y0, h):

    return rk2(equation, x0, y0, h, alpha = 1/2, beta = 1/2, c1 = 0, c2 = 1)

def ralston(equation, x0, y0, h):

    return rk2(equation, x0, y0, h, alpha=2/3, beta=2/3, c1=1/4, c2=3/4)


def rk4(equation, x0, y0, h):

    x1 = x0 + h
    k1 = h*f(equation, x0, y0)
    k2 = h*f(equation, x0 + h/2 , y0 + k1/2)
    k3 = h*f(equation, x0 + h/2 , y0 + k2/2)
    k4 = h*f(equation, x0 + h, y0 + k3)

    k = (k1 + 2*k2 + 2*k3 + k4)/6

    y1 = y0 + k

    return x1, y1

