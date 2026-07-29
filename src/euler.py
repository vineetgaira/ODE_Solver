def f(x, y):
    """
    Here you are going to provide the f(x, y) = dy/dx.
    It will return the value of the functions. """

    return x + y

def euler_method(x, y, h):
    """
    This is returns the euler's value to find y(x).
    You can iterate it as many times as you want.
    """

    return y + h*f(x, y)


