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
    pass

def get_initial_x():
    pass

def get_initial_y():
    pass

def get_target_x():
    pass

def get_step_size():
    pass

def get_exact_solution():
    pass

def confirm_continue():
    pass