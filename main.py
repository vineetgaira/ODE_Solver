from colorama import Fore
"""This is the main function that will lead all the other methods."""
from src.utils import get_user_input
from src.euler import euler_method
from src.constants import DECIMAL_PLACES

def menu():
    x0, y0 = 0, 1
    h = 0.1
    x1 = x0 + h 
    x2 = x1 + h
    x3 = x2 + h
    while True:
        print("1. Euler's method.\n"
              "2. Modified Euler's method\n" \
              "3. Runge Kutta 4 (RK4)\n" \
              "4. Exit.")
        choice = get_user_input()
        if choice == 1:
            # Euler's Method
            y1 = euler_method(x0, y0, h)
            print(Fore.CYAN+f"Y({Fore.YELLOW+str(x1)}) :{Fore.GREEN+str(round(y1, DECIMAL_PLACES))}")

        elif choice == 2:
            # Modified Euler's method
            pass
        elif choice == 3:
            # RK4
            pass
        else:
            return
    

menu()
        
        
        
