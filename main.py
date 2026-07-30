"""This file will store the main project loop."""
from src.menu import menu
from src.input_handler import user_ode

def main():
    menu()
    user_ode()
    

if __name__ =="__main__":
    main()