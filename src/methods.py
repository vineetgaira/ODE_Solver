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

def midpoint(equation, x0, y0, h):
    k1 = h*f(equation, x0, y0)
    k2 = h*f(equation, x0 + h/2 , y0 + k1/2)

    y1 = y0 + k2

    return {"k1": k1,
            "k2": k2,
            "y1": y1}


def rk2(equation, x0, y0, h, a, b, c1, c2):

    x1 = x0 + h
    
    k1 = f(equation, x0, y0)
    k2 = f(equation, x0 + a*h, y0 + b*h*k1)

    y1 = y0 + h*(c1*k1 + c2*k2)

    return x1, y1

def rk4(equation, x0, y0, h):
    pass
    k1 = h*f(equation, x0, y0)
    k2 = h*f(equation, x0 + h/2 , y0 + k1/2)
    k3 = h*f(equation, x0 + h/2 , y0 + k2/2)
    k4 = h*f(equation, x0 + h, y0 + k3)

    k = (k1 + 2*k2 + 2*k3 + k4)/6

    y1 = y0 + k

    return {"k1": k1,
            "k2": k2,
            "k3": k3,
            "k4": k4,
            "k": k,
            "y1": y1}

# rk2_family= {
#     "heun":rk2 (equation, x0, y0, h, 1, 1, 1/2, 1/2),
#     "midpoint":rk2(equation, x0, y0, h, 1/2, 1/2, 0, 1),
#     "raltson":rk2(equation, x0, y0, h, 2/3, 2/3, 1/4, 3/4)
# }