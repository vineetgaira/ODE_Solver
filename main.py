"""This file will store the main project loop."""
import colorama
from colorama import Fore
colorama.init(autoreset= True)

from src.constants import MAIN_MENU, METHODS_MENU, PLOT_MENU, SETTINGS, COMPARE_MENU
from src.solver import solve_with_method, compare_methods
from src.utils import clear_screen, pause
from src.input_handler import get_menu_choice, get_all_inputs
from src.menu import show_banner, show_main_menu, show_solver_menu, show_help_menu, show_settings_menu, show_graph_menu,show_compare_menu, show_info_menu
from src.display import display_method_information, display_comparison, display_solution, display_error, display_success
from src.exporter import save_problem, save_solutions
from src.input_handler import get_valid_float
from src.graph import plot_solution, plot_comparison, save_graph
from src.settings import load_settings, get_setting, set_settings


current_problem = None
history = None
method = None
solutions = None
last_plot = None

prompt = "Choice :"
def main():
    global current_problem, history, method, solutions, last_plot
    load_settings()
    show_banner()
    input() 
    clear_screen()
    while True:
        show_main_menu()
        choice = get_menu_choice(MAIN_MENU, prompt)
        if choice == "new":
            current_problem = get_all_inputs()
            if get_setting("save_automatically"):
                save_problem(current_problem)
            display_success("Problem loaded.")
            pause()
        
        elif choice == "solve":
            if current_problem is None:
                display_error("No problem loaded.")
            else:
                show_solver_menu()
                method = get_menu_choice(METHODS_MENU, prompt)
                history = solve_with_method(method, current_problem["equation"], current_problem["x0"],
                            current_problem["y0"], current_problem["target_x"], current_problem["step_size"])
                display_solution(history, method, current_problem["equation"] )
                
            pause()
            clear_screen()
        elif choice == "compare": 
            if current_problem is None:
                display_error("No problem loaded.")
            else:
                show_compare_menu()
                compare_choice = get_menu_choice(COMPARE_MENU, prompt)
                if compare_choice == "all":
                    solutions = compare_methods(current_problem["equation"], current_problem["x0"], 
                                                current_problem["y0"], current_problem["target_x"], current_problem["step_size"])
                    display_comparison(solutions, current_problem["equation"], current_problem["target_x"], exact_solution=None)
                    if get_setting("save_automatically"):
                        save_solutions(current_problem, solutions)
                elif compare_choice == "exact":
                    solutions = compare_methods(current_problem["equation"], current_problem["x0"], 
                                                current_problem["y0"], current_problem["target_x"], current_problem["step_size"])
                    exact = get_valid_float(Fore.LIGHTCYAN_EX + "Exact Solution: ")
                    display_comparison(solutions, current_problem["equation"], current_problem["target_x"], exact_solution=exact)
                    if get_setting("save_automatically"):
                        save_solutions(current_problem, solutions)
            pause()
            clear_screen()
        elif choice == "plot":
            show_graph_menu()
            plot_choice = get_menu_choice(PLOT_MENU, prompt)
            if plot_choice == "solution":
                if history is None:
                    display_error("No solution to plot yet. Solve a method first.")
                else:
                    plot_solution(history ,method, current_problem['equation'])
                    last_plot = {"type": "solution", "history": history, "method": method,
                             "equation": current_problem["equation"]}
            elif plot_choice == "comparison":
                if solutions is None:
                    display_error("No comparison to plot yet. Run compare method first.")
                else:
                    plot_comparison(solutions, current_problem["equation"])
                    last_plot = {"type": "comparison", "solutions": solutions,
                             "equation": current_problem["equation"]}
            elif plot_choice == "save":
                if last_plot is None:
                    display_error("No plot to save yet. Plot something first.")
                else:
                    filepath = save_graph(last_plot)
                    display_success(f"Graph saved to {filepath}")
            else:
                display_error(f"Unrecognized plot option: {plot_choice}")
                pause()
        elif choice == "info":
            show_info_menu()
            method = get_menu_choice(METHODS_MENU, prompt)
            display_method_information(method)
            pause()
            clear_screen()

        elif choice == "settings":
            show_settings_menu()
            setting_choice = get_menu_choice(SETTINGS, prompt)
            if setting_choice == "precision":
                new_val = int(get_valid_float(Fore.LIGHTCYAN_EX + "New decimal precision: "))
                set_settings("precision", new_val)
            elif setting_choice == "colour":
                set_settings("colour", not get_setting("colour"))
                print(Fore.GREEN + f"Colour output is now {'ON' if get_setting('colour') else 'OFF'}")
            elif setting_choice == "save_res":
                set_settings("save_automatically", not get_setting("save_automatically"))
                print(Fore.GREEN + f"Auto-save is now {'ON' if get_setting('save_automatically') else 'OFF'}")
            elif setting_choice == "graph_style":
                new_style = "scatter" if get_setting("graph_style") == "line" else "line"
                set_settings("graph_style", new_style)
                print(Fore.GREEN + f"Graph style is now {new_style}")
            elif setting_choice == "return":
                continue
            pause()
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