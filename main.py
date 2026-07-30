"""This file will store the main project loop."""
import colorama
from colorama import Fore
colorama.init(autoreset= True)

import time
from src.input_handler import get_menu_choice
from src.menu import show_banner, show_main_menu, show_solver_menu, show_help_menu, show_settings_menu, show_graph_menu,show_compare_menu, show_info_menu

MAIN_MENU={
    1: show_solver_menu,
 2: show_compare_menu,
 3: show_graph_menu,
 4: show_info_menu,
 5: show_settings_menu,
  6: show_help_menu
}


def main():
    show_banner()
    input() 
    show_main_menu()
    while True:
        choice = get_menu_choice()
        if choice == 7:
            print(Fore.CYAN+"Thanks for using.")
            return
        else:
            MAIN_MENU[choice]()

if __name__ =="__main__":
    main()