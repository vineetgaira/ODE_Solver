from colorama import Fore

import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():    
    input(Fore.LIGHTCYAN_EX + "Press [ENTER] to return.")
