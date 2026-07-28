DECIMAL_PLACES = 7

def f(x, y):
    """
    This here takes the main function.
    It returns the value of the function.
    """

    return x + y

def rk4(x, y, h):
    """
    This will compute k1, k2, k3, k4 and k and in the end it returns the value of the next y.
    y1 = y0 + k
    """

    k1 = h*f(x, y)
    k2 = h*f(x+h/2, y+k1/2)
    k3 = h*f(x+h/2, y+k2/2)
    k4 = h*f(x+h, y+k3)

    k = (k1+ 2*k2+ 2*k3 + k4)/6

    return y + k

x0, y0 = 0, 1
h=0.1
x1 = x0 + h
x2 = x1 + h
x3 = round(x2+h, 2)

y1= rk4(x0, y0, h)
print(f"Y({x1}) : {round(y1, DECIMAL_PLACES)}")
y2=rk4(x1, y1, h)
print(f"Y({x2}) : {round(y2, DECIMAL_PLACES)}")
y3 = rk4(x2, y2, h)
print(f"Y({x3}) : {round(y3, DECIMAL_PLACES)}")