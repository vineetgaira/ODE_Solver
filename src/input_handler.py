"""This file handles user input"""

import sympy 
from sympy import symbols, sympify, pprint

def user_ode():

    x, y = symbols('x y')

    ode = input("Give an ODE in terms of x and y: ")

    expression = sympify(ode)
    pprint(expression, use_unicode = True)




    