import colorama 
from colorama import Fore, Style
colorama.init(autoreset= True)
from src.ascii_art import banner

def show_banner():
    print(Fore.LIGHTCYAN_EX + banner)

def show_main_menu():

    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "             NUMERICAL ODE SOLVER")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.LIGHTCYAN_EX + "Solve Initial Value Problem")
    print(Fore.WHITE + "  [2] " + Fore.LIGHTCYAN_EX + "Compare Numerical Methods")
    print(Fore.WHITE + "  [3] " + Fore.LIGHTCYAN_EX + "Plot Solution Graph")
    print(Fore.WHITE + "  [4] " + Fore.LIGHTCYAN_EX + "Veiw Method Information")
    print(Fore.WHITE + "  [5] " + Fore.LIGHTCYAN_EX + "Settings")
    print(Fore.WHITE + "  [6] " + Fore.LIGHTCYAN_EX + "Help")
    print(Fore.WHITE + "  [7] " + Fore.RED + "Exit")


def show_solver_menu():
    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "           CHOOSE NUMERICAL METHOD")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.LIGHTCYAN_EX + "Euler Method")
    print(Fore.WHITE + "  [2] " + Fore.LIGHTCYAN_EX + "Modified Euler Method/Heun")
    print(Fore.WHITE + "  [3] " + Fore.LIGHTCYAN_EX + "Midpoint Method")
    print(Fore.WHITE + "  [4] " + Fore.LIGHTCYAN_EX + "RK2")
    print(Fore.WHITE + "  [5] " + Fore.LIGHTCYAN_EX + "RK4")

def show_graph_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "     Select Plot Type")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.LIGHTCYAN_EX + "Plot numerical solution")
    print(Fore.WHITE + "  [2] " + Fore.LIGHTCYAN_EX + "Plot exact solution")
    print(Fore.WHITE + "  [3] " + Fore.LIGHTCYAN_EX + "Plot both")

def show_settings_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "     Settings")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.LIGHTCYAN_EX + "Decimal Precision")
    print(Fore.WHITE + "  [2] " + Fore.LIGHTCYAN_EX + "Output colour")
    print(Fore.WHITE + "  [3] " + Fore.LIGHTCYAN_EX + "Save results automatically")
    print(Fore.WHITE + "  [4] " + Fore.LIGHTCYAN_EX + "Graph style")
    print(Fore.WHITE + "  [5] " + Fore.RED + "Return")
    

def show_help_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "    Supported Functions")
    print(Fore.MAGENTA + "=" * 26)
                    
    print(Fore.LIGHTCYAN_EX + "sin(x)")
    print(Fore.LIGHTCYAN_EX + "cos(x)")
    print(Fore.LIGHTCYAN_EX + "tan(x)")
    print(Fore.LIGHTCYAN_EX + "exp(x)")
    print(Fore.LIGHTCYAN_EX + "sqrt(x)")
    print(Fore.LIGHTCYAN_EX + "log(x)")
    print(Fore.LIGHTCYAN_EX + "pi")
    print(Fore.LIGHTCYAN_EX + "e")

def show_compare_menu():
    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "        COMPARE METHODS")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.LIGHTCYAN_EX + "Compare All Methods")
    print(Fore.WHITE + "  [2] " + Fore.LIGHTCYAN_EX + "Compare With Exact Solution")
    print(Fore.WHITE + "  [3] " + Fore.LIGHTCYAN_EX + "Compare Different Step Sizes")
    print(Fore.WHITE + "  [4] " + Fore.LIGHTCYAN_EX + "Back")

def show_info_menu():
    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "     CHOOSE NUMERICAL METHOD TO GET INFO")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.LIGHTCYAN_EX + "Euler Method")
    print(Fore.WHITE + "  [2] " + Fore.LIGHTCYAN_EX + "Modified Euler Method/Heun")
    print(Fore.WHITE + "  [3] " + Fore.LIGHTCYAN_EX + "Midpoint Method")
    print(Fore.WHITE + "  [4] " + Fore.LIGHTCYAN_EX + "RK2")
    print(Fore.WHITE + "  [5] " + Fore.LIGHTCYAN_EX + "RK4")




