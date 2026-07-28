"""This is the main function that will lead all the other methods."""
from src.utils import get_user_input

def menu():
    while True:
        print("1. Euler's method.\n"
              "2. Modified Euler's method\n" \
              "3. Runge Kutta 4 (RK4)\n" \
              "4. Exit.")
        choice = get_user_input()
        if choice == 1:
            # Euler's Method
            pass
        elif choice == 2:
            # Modified Euler's method
            pass
        elif choice == 3:
            # RK4
            pass
        else:
            return
    

menu()
        
        
        
