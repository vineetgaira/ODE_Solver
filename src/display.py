"""This file will only store function that will display to the screen."""

import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from src.constants import METHOD_INFO

def display_history(history):
    iteration = 0
    for i in history:
        iteration +=1
        print(Fore.GREEN + f"Iteration {iteration} : x{iteration}, y{iteration} = {Fore.LIGHTBLUE_EX + str(i)}")
        
def display_step():
    pass

def display_solution():
    pass

def display_comparison():
    pass

def display_error():
    pass

def display_success():
    pass

def display_method_information(method):
   
   for key, value in METHOD_INFO[method].items():
       print(f"{Fore.LIGHTYELLOW_EX + key} : {Fore.LIGHTGREEN_EX + value}")
       

def display_separator():
    pass