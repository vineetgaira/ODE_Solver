"""This file will store the main project loop."""
import colorama
from colorama import Fore
colorama.init(autoreset= True)

from src.constants import MAIN_MENU, METHODS_MENU, PLOT_MENU, SETTINGS, COMPARE_MENU
from src.solver import solve_with_method, compare_methods
from src.utils import clear_screen, pause
from src.input_handler import get_menu_choice, get_all_inputs
from src.menu import show_banner, show_main_menu, show_solver_menu, show_help_menu, show_settings_menu, show_graph_menu,show_compare_menu, show_info_menu
from src.display import display_history, display_method_information, display_comparison, display_solution

current_problem = None

prompt = "Choice :"
def main():
    show_banner()
    input() 
    clear_screen()
    while True:
        show_main_menu()
        choice = get_menu_choice(MAIN_MENU, prompt)
        if choice == "new":
          current_problem = get_all_inputs()
          print(Fore.GREEN + "Problme Loaded.")
          pause()
        
        elif choice == "solve":
            if current_problem is None:
                print(Fore.RED + "No problem laoded.")
            show_solver_menu()
            method = get_menu_choice(METHODS_MENU, prompt)
            history = solve_with_method(method, current_problem["equation"], current_problem["x0"],
                           current_problem["y0"], current_problem["target_x"], current_problem["step_size"])
            display_history(history)
            pause()
            clear_screen()
        elif choice == "compare":
            if current_problem is None:
                print(Fore.RED + "No problme loaded.")
            show_compare_menu()
            compare_choice = get_menu_choice(COMPARE_MENU, prompt)
            if compare_choice == "all":
                solutions = compare_methods(current_problem["equation"], current_problem["x0"], 
                                            current_problem["y0"], current_problem["target_x"], current_problem["step_size"]  )
                display_comparison(solutions)
            pause()
            clear_screen()
        elif choice == "plot":
            show_graph_menu()
            get_menu_choice(PLOT_MENU, prompt)
            clear_screen()
        elif choice == "info":
            show_info_menu()
            method = get_menu_choice(METHODS_MENU, prompt)
            display_method_information(method)
            pause()
            clear_screen()
        elif choice == "settings":
            show_settings_menu()
            get_menu_choice(SETTINGS, prompt)
            clear_screen()
        elif choice == "help":
            show_help_menu()
            pause()
            clear_screen()
        elif choice == "exit":
            print(Fore.LIGHTCYAN_EX+ "Thanks for using.")
            return
    


if __name__ =="__main__":
    main()