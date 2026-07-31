"""This file handles user input"""

import colorama
from colorama import Fore
colorama.init(autoreset= True)

def get_menu_choice(options: dict, prompt: str):
    valid_choices = set(options.keys())
    while True:
        try:
            choice = int(input(Fore.LIGHTCYAN_EX + prompt))
            if choice in valid_choices:
                return options[choice ]
            else:
                print(Fore.RED+"Invalid Choice! Try again.")
        except ValueError:
            print(Fore.RED+"Invalid Choice! Try again.")

def get_equation():
    
    equation = input("Equation (dy/dx = )")
    return equation 

def get_initial_x():
    while True:
        try:
            initial_x = float(input("Initial x (x₀) : "))
            if initial_x != 0:
                return initial_x
            else:
                print("Invalid value! Must be greater than 0.")
        except ValueError:
            print("Invalid value! Must be a number.")

def get_initial_y():

    while True:
        try:
            initial_y = float(input("Initial y (y₀) : "))
            if initial_y != 0:
                return initial_y
            else:
                print("Invalid value! Must be greater than 0.")
        except ValueError:
            print("Invalid value! Must be a number.")
  

def get_target_x():
    while True:
        try:
            target_x = float(input("Target x : "))
            if target_x != 0:
                return target_x
            else:
                print("Invalid value! Must be greater than 0.")
        except ValueError:
            print("Invalid value! Must be a number.")

def get_step_size():
    while True:
        try:
            step_size = float(input("Step size (h) : "))
            if step_size > 0:
                return step_size
            else:
                print("Invalid value! Must be greater than 0.")
        except ValueError:
            print("Invalid value! Must be a number.")

def get_exact_solution():
    while True:
        try:
            exact_solution = float(input("Enter the exact solutin : "))
            if exact_solution != 0:
                return exact_solution
            else:
                print("Invalid value! Must be greater than 0.")
        except ValueError:
            print("Invalid value! Must be a number.")


def all_initial_values(equation, initial_x, initial_y, target_x, step_size):

    values = {
    "equation": equation,
    "x0": initial_x,
    "y0": initial_y,
    "target_x": target_x,
    "step_size": step_size
    }

    return values

