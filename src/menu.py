import colorama 
from colorama import Fore, Style
colorama.init(autoreset= True)
from src.ascii_art import banner

def show_banner():
    print(Fore.LIGHTCYAN_EX + banner)

def show_menu():

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


def method_menu():
    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "           CHOOSE NUMERICAL METHOD")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Euler Method")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Modified Euler Method")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Heun Method")
    print(Fore.WHITE + "  [4] " + Fore.CYAN + "Midpoint Method")
    print(Fore.WHITE + "  [5] " + Fore.CYAN + "RK2")
    print(Fore.WHITE + "  [6] " + Fore.CYAN + "RK4")

def graph_menu():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "     Select Plot Type")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Plot numerical solution")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Plot exact solution")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Plot both")


