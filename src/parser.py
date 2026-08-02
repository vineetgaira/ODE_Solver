"""This file will store the input funtion for the equations and will parse them"""

from sympy import symbols
from sympy.parsing.sympy_parser import (standard_transformations, implicit_multiplication_application, convert_xor)
from sympy.parsing.sympy_parser import parse_expr
from sympy import SympifyError

ALLOWED_CHARS = set('xy0123456789+-*/.^ ')
ALLOWED_WORDS = {'sin', 'cos', 'tan', 'exp', 'log','pi', 'sqrt', 'e' }


