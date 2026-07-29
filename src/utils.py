import colorama 
from colorama import Fore, Style
colorama.init(autoreset=True)

def get_user_input():
    valid_choices = {1, 2, 3, 4}
    try:
        user = int(input(Fore.BLUE+"Enter your choice:"))
        if user in valid_choices:
            return user
        else:
            print(Fore.RED+Style.BRIGHT+"Please enter a valid choice."+Style.RESET_ALL)
    except ValueError:
        print(Fore.RED+Style.BRIGHT+"Please enter a valid choice."+Style.RESET_ALL)
