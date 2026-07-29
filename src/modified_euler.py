from src.function import f

def predictor(x, y, h):

    """
    This is returns the euler's value to find y(x).
    You can iterate it as many times as you want.
    In modified euler this term is called predictor.
    It predicts the initial value.
    """

    return y + h*f(x, y)


def corrector(x, y, y_pred, h):
    """
    This here is the corrector usually you can run multiple iterations of this until the values match.
    It takes the value of y_predictor (y_1_0).

    """

    return y_pred + h/2* (f(x, y) + f(x, y_pred))
