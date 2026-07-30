"""This file handles user input"""

import colorama
from colorama import Fore
colorama.init(autoreset= True)

def get_menu_choice():
    valid_choices = {1, 2, 3, 4, 5, 6, 7}
    while True:
        try:
            choice = int(input(Fore.LIGHTCYAN_EX + "Choice: "))
            if choice in valid_choices:
                return choice 
            else:
                print(Fore.RED+"Invalid Choice! Try again.")
        except ValueError:
            print(Fore.RED+"Invalid Choice! Try again.")

def get_method():
    valid_choices = {1, 2, 3, 4, 5}
    while True:
        try:
            choice = int(input(Fore.LIGHTCYAN_EX + "Choice: "))
            if choice in valid_choices:
                return choice 
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