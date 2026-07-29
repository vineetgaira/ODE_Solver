from src.function import f
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

