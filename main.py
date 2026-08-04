"""This file will store the main project loop."""
import colorama
from colorama import Fore
colorama.init(autoreset= True)

from src.constants import MAIN_MENU, METHODS_MENU, PLOT_MENU, SETTINGS, COMPARE_MENU
from src.utils import clear_screen
from src.input_handler import get_menu_choice, get_all_inputs
from src.menu import show_banner, show_main_menu, show_solver_menu, show_help_menu, show_settings_menu, show_graph_menu,show_compare_menu, show_info_menu


prompt = "Choice :"
def main():
    show_banner()
    input() 
    clear_screen()
    while True:
        show_main_menu()
        choice = get_menu_choice(MAIN_MENU, prompt)
        if choice == "solve":
            initial_values = get_all_inputs()
            show_solver_menu()
            method = get_menu_choice(METHODS_MENU, prompt)
            clear_screen()
        elif choice == "compare":
            show_compare_menu()
            get_menu_choice(COMPARE_MENU, prompt)
            clear_screen()
        elif choice == "plot":
            show_graph_menu()
            get_menu_choice(PLOT_MENU, prompt)
            clear_screen()
        elif choice == "info":
            show_info_menu()
            get_menu_choice(METHODS_MENU, prompt)
            clear_screen()
        elif choice == "settings":
            show_settings_menu()
            get_menu_choice(SETTINGS, prompt)
            clear_screen()
        elif choice == "help":
            show_help_menu()
            input(Fore.LIGHTCYAN_EX+"<<< Press ENTER to return >>>")
            clear_screen()
        elif choice == "exit":
            print(Fore.LIGHTCYAN_EX+ "Thanks for using.")
            return
    


if __name__ =="__main__":
    main()