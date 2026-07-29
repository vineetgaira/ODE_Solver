import colorama
colorama.init(autoreset=True)
from colorama import Fore,Style
"""This is the main function that will lead all the other methods."""
from src.utils import get_user_input
from src.euler import euler_method
from src.modified_euler import corrector
from src.runge_kutta_4 import rk4
from src.constants import DECIMAL_PLACES


def menu():
    x0, y0 = 0, 1
    h = 0.1
    x1 = x0 + h 
    x2 = x1 + h
    x3 = x2 + h
    while True:
        print(Fore.BLUE+"1. Euler's method.\n"
              "2. Modified Euler's method\n" \
              "3. Runge Kutta 4 (RK4)\n" \
              "4. Exit.")
        choice = get_user_input()
        if choice == 1:
            y1 = euler_method(x0, y0, h)
            print(Fore.CYAN+f"Y({Fore.YELLOW+str(x1)}) :{Fore.GREEN+str(round(y1, DECIMAL_PLACES))}")
  
        elif choice == 2:
            y1 = euler_method(x0, y0, h)
            y_next = corrector(x0, y0, y1, h )
            print(Fore.CYAN+f"Y({Fore.YELLOW+str(x1)}) :{Fore.GREEN+str(round(y_next, DECIMAL_PLACES))}")

        elif choice == 3:
            y_rk = rk4(x0, y0, h)
            print(Fore.CYAN+f"Y({Fore.YELLOW+str(x1)}) :{Fore.GREEN+str(round(y_rk, DECIMAL_PLACES))}")
        elif choice == 4:
            return
        else:
            print(Fore.RED+Style.BRIGHT+"Please enter a valid choice"+Style.RESET_ALL)
    

menu()
        
        
        
