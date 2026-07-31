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
            if initial_x > 0:
                return initial_x
            else:
                print("Invalid value! Must be greater than 0.")
        except ValueError:
            print("Invalid value! Must be a number.")

def get_initial_y():

    initial_y = float(input("Initial y (y₀) : "))

    return initial_y   

def get_target_x():
     
    target_x = float(input("Target x : "))

    return  target_x

def get_step_size():

    step_size = float(input("Step size (h) : "))

    return step_size  

def get_exact_solution():

    exact_solution = float(input("Please enter the exact solution : "))

    return exact_solution

def confirm_continue():
    pass