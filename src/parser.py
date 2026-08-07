"""This file will store the input funtion for the equations and will parse them"""

from colorama import Fore, Style
from sympy import symbols
from sympy.parsing.sympy_parser import (standard_transformations, implicit_multiplication_application, convert_xor)
from sympy.parsing.sympy_parser import parse_expr
from sympy import SympifyError

TRANSFORMS = standard_transformations + (
implicit_multiplication_application, convert_xor
)

ALLOWED_CHARS = set('xy0123456789+-*/.^() ')
ALLOWED_WORDS = {'sin', 'cos', 'tan', 'exp', 'log','pi', 'sqrt', 'e' }

x, y = symbols('x y')

def is_valid_charset(eq: str) -> bool:

    if not eq.strip():
        return False
    if len(eq) > 200:
        return False
    return set(eq.replace(' ', '')) <= (ALLOWED_CHARS | set(''.join(ALLOWED_WORDS)))

def safe_parse(eq):

    local_dict = {'x': x, 'y': y}

    return parse_expr(eq,  local_dict=local_dict, transformations=TRANSFORMS)

def has_valid_symbols(expr) -> bool:
    allowed = {x, y}
    found = expr.free_symbols
    return len(found) > 0 and found <= allowed

def get_equation():
    while True:
        raw = input(Fore.LIGHTCYAN_EX + 'Equation (dy/dx = ) : ')
        if not is_valid_charset(raw):
            print(Fore.RED + 'Invalid characters! Use only x, y, numbers and + - * / ^ ( )')
            continue
        try:
            expr = safe_parse(raw)
        except (SympifyError, TypeError, SyntaxError):
            print(Fore.RED + 'Could not parse that expression. Check your parentheses and operators.')
            continue
        if not has_valid_symbols(expr):
            print(Fore.RED + 'Equation must use only x and y, and cannot be a constant.')
            continue
        return expr

def f(equation, x0, y0):
    # Okay so this will solve it with initital values 
    # for example f(x, y) = x + y where x = 0, y = 2 the value will bet 0 + 2 = 2
    result = equation.subs({x: x0, y: y0}).evalf()
    real_part, imag_part = result.as_real_imag()
    return float(real_part)

