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
    
    equation = input("Equation (dy/dx = ) : ")
    return equation 

def get_valid_float(prompt, is_valid, error_message):
    while True:
        try:
            value = float(input(prompt))
            if is_valid(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid value! Must be a number.")

initial_x = get_valid_float("Initial x (x₀) : ", lambda v: v != 0, "Invalid value! Must not be 0.")
initial_y = get_valid_float("Initial y (y₀) : ", lambda v: v != 0, "Invalid value! Must not be 0.")
target_x = get_valid_float("Target x : ", lambda v: v != 0, "Invalid value! Must not be 0.")
step_size = get_valid_float("Step size (h) : ", lambda v: v > 0, "Invalid value! Must be greater than 0.")
exact_solution = get_valid_float("Enter the exact solution : ", lambda v: v != 0, "Invalid value! Must not be 0.")

def all_initial_values(equation, initial_x, initial_y, target_x, step_size):

    values = {
    "equation": equation,
    "x0": initial_x,
    "y0": initial_y,
    "target_x": target_x,
    "step_size": step_size
    }

    return values

