"""This file handles user input"""

import colorama
from colorama import Fore
colorama.init(autoreset=True)
from src.parser import get_equation

def get_menu_choice(options: dict, prompt: str):
    valid_choices = set(options.keys())
    while True:
        try:
            choice = int(input(Fore.LIGHTCYAN_EX + prompt))
            if choice in valid_choices:
                return options[choice]
            else:
                print(Fore.RED + "Invalid Choice! Try again.")
        except ValueError:
            print(Fore.RED + "Invalid Choice! Try again.")

def get_valid_float(prompt, is_valid=lambda v: True, error_message="Invalid value! Must be a number."):
    while True:
        try:
            value = float(input(Fore.LIGHTCYAN_EX + prompt))
            if is_valid(value):
                return value
            else:
                print(Fore.RED + error_message)
        except ValueError:
            print(Fore.RED + "Invalid value! Must be a number.")

def collect_initial_values(equation, initial_x, initial_y, target_x, step_size):

    return {
    "equation": equation,
    "x0": initial_x,
    "y0": initial_y,
    "target_x": target_x,
    "step_size": step_size,
    }

    
def get_all_inputs():
    equation = get_equation()
    initial_x = get_valid_float("Initial x (x₀) : ")
    initial_y = get_valid_float("Initial y (y₀) : ")
    target_x = get_valid_float("Target x : ")
    

    step_size = get_valid_float(
        "Step size (h) : ",
        lambda v: v > 0,
        "Invalid value! Must be greater than 0."
    )

    return collect_initial_values(equation, initial_x, initial_y, target_x, step_size,)
