import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from src.constants import METHOD_INFO
from rich.console import Console
from rich.table import Table

from src.settings import get_setting


console = Console()

def display_history(history):
    step = 0
    for i in history:
        step +=1
        print(Fore.GREEN + f"Step {step} : x{step}, y{step} = {Fore.LIGHTBLUE_EX + str(i)}")
        

def display_solution(history, method_name, equation, exact_solution = None):
    table = Table(title=f"{method_name.upper()} Solution dy/dx = {equation}")
    table.add_column("Step", justify="right", style="cyan")
    table.add_column("x", justify="right")
    table.add_column("y", justify="right", style="green")

    for i, (xi, yi) in enumerate(history):
        table.add_row(str(i), f"{round(xi, get_setting("precision"))}", f"{round(yi, get_setting("precision"))}")

    console.print(table)

    final_x, final_y = history[-1]

    if exact_solution is not None:
        error = abs(final_y - exact_solution)
        console.print(
            f"[bold]Final:[/bold] y({round(final_x, get_setting("precision"))}) = {round(final_y, get_setting("precision"))}   "
            f"[bold]Exact:[/bold] {exact_solution}   "
            f"[bold red]Error:[/bold red] {round(error, get_setting("precision"))}"
        )
    else:
        console.print(f"[bold]Final:[/bold] y({round(final_x, get_setting("precision"))}) = {round(final_y, get_setting("precision"))}")

def display_comparison(solutions, equation, target_x, exact_solution = None):
    table= Table(title=f"Method Comparison: dy/dx = {equation}, target_x = {target_x}")
    table.add_column("Method", style="cyan")
    table.add_column("Final x", justify="right")
    table.add_column("Final y", justify="right", style="green")

    if exact_solution is not None:
        table.add_column("Error", justify="right", style="red")

    for name, history in solutions.items():
        fx, fy = history[-1]
        row = [name, f"{round(fx, get_setting("precision"))}", f"{round(fy, get_setting("precision"))}"]
        if exact_solution is not None:
            row.append(f"{round(abs(fy-exact_solution), get_setting("precision"))})")
        table.add_row(*row)

    console.print(table)

def display_error(message):
    console.print(f"[bold red]Error: {message}[/bold red]")

def display_success(message):
    console.print(f"[bold green]Success: {message}[/bold green]")

def display_method_information(method):
   
   for key, value in METHOD_INFO[method].items():
       print(f"{Fore.LIGHTYELLOW_EX + key} : {Fore.LIGHTGREEN_EX + value}")

def display_separator():
    console.print("_"*46, style="dim")

