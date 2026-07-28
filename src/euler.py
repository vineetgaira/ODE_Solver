DECIMAL_PLACES = 7

def f(x, y):
    """
    Here you are going to provide the f(x, y) = dy/dx.
    It will return the value of the functions. """

    return x + y

def euler(x, y, h):
    """
    This is returns the euler's value to find y(x).
    You can iterate it as many times as you want.
    """

    return y + h*f(x, y)

x0, y0 = 0, 1
h = 0.1
x1 = x0 + h 
x2 = x1 + h
x3 = x2 + h

y1 = euler(x0, y0, h)
print(f"Y({x1}) :{round(y1, DECIMAL_PLACES)}")

y2 = euler(x1, y1, h)
print(f"Y({x2}) :{round(y2, DECIMAL_PLACES)}")

y3 = euler(x2, y2, h)
print(f"Y({round(x3, 1)}) :{round(y3, DECIMAL_PLACES)}")