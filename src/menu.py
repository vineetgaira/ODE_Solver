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

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Solve Initial Value Problem")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Compare Numerical Methods")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Plot Solution Graph")
    print(Fore.WHITE + "  [4] " + Fore.CYAN + "Veiw Method Information")
    print(Fore.WHITE + "  [5] " + Fore.CYAN + "Settings")
    print(Fore.WHITE + "  [6] " + Fore.CYAN + "Help")
    print(Fore.WHITE + "  [7] " + Fore.RED + "Exit")


def show_solver_menu():
    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "           CHOOSE NUMERICAL METHOD")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Euler Method")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Modified Euler Method/Heun")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Midpoint Method")
    print(Fore.WHITE + "  [4] " + Fore.CYAN + "RK2")
    print(Fore.WHITE + "  [5] " + Fore.CYAN + "RK4")

def show_graph_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "     Select Plot Type")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Plot numerical solution")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Plot exact solution")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Plot both")

def show_settings_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "     Settings")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Decimal Precision")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Output colour")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Save results automatically")
    print(Fore.WHITE + "  [4] " + Fore.CYAN + "Graph style")
    print(Fore.WHITE + "  [5] " + Fore.RED + "Return")
    

def show_help_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "    Supported Functions")
    print(Fore.MAGENTA + "=" * 26)
                    
    print(Fore.CYAN + "sin(x)")
    print(Fore.CYAN + "cos(x)")
    print(Fore.CYAN + "tan(x)")
    print(Fore.CYAN + "exp(x)")
    print(Fore.CYAN + "sqrt(x)")
    print(Fore.CYAN + "log(x)")
    print(Fore.CYAN + "pi")
    print(Fore.CYAN + "e")

def show_compare_menu():
    print(Fore.CYAN+"Will be added soon.")
    pass            

def show_info_menu():
    show_solver_menu()



