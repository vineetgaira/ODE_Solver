import colorama 
from colorama import Fore, Style
colorama.init(autoreset= True)
from src.ascii_art import banner

def show_banner():
    print(Fore.LIGHTCYAN_EX + banner)