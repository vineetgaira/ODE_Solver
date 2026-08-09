"""This is a general helper module to make things easy."""
from colorama import Fore

import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():    
    input(Fore.LIGHTCYAN_EX + "Press [ENTER] to return.")

def format_number():
    pass

def timer():
    pass

def round_value():
    pass

def print_line():
    pass

def get_current_time():
    pass

def calculate_steps():
    pass