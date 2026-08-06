"""This file will only store function that will display to the screen."""

import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from src.constants import METHOD_INFO
from rich.console import Console
from rich.table import Table

DECIMAL_PRECISION = 5

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
        table.add_row(str(i), f"{round(xi, DECIMAL_PRECISION)}", f"{round(yi, DECIMAL_PRECISION)}")

    console.print(table)

    final_x, final_y = history[-1]

    if exact_solution is not None:
        error = abs(final_y - exact_solution)
        console.print(
            f"[bold]Final:[/bold] y({round(final_x, DECIMAL_PRECISION)}) = {round(final_y, DECIMAL_PRECISION)}   "
            f"[bold]Exact:[/bold] {exact_solution}   "
            f"[bold red]Error:[/bold red] {round(error, DECIMAL_PRECISION)}"
        )
    else:
        console.print(f"[bold]Final:[/bold] y({round(final_x, DECIMAL_PRECISION)}) = {round(final_y, DECIMAL_PRECISION)}")

def display_comparison(solutions, equation, target_x, exact_solution = None):
    table= Table(title=f"Method Comparison: dy/dx = {equation}, terget_x = {target_x}")
    table.add_column("Method", style="cyan")
    table.add_column("Final x", justify="right")
    table.add_column("Final y", justify="right", style="green")

    if exact_solution is not None:
        table.add_column("Error", justify="right", style="red")

    for name, history in solutions.items():
        fx, fy = history[-1]
        row = [name, f"{round(fx, DECIMAL_PRECISION)}", f"{round(fy, DECIMAL_PRECISION)}"]
        if exact_solution is not None:
            row.append(f"{round(abs(fy-exact_solution), DECIMAL_PRECISION)})")
        table.add_row(*row)

    console.print(table)

def display_error(message):
    console.print(f"[bold red]Error:[/bold red] {message}")

def display_success(message):
    console.print(f"[bold green]Success:[/bold green] {message}")

def display_method_information(method):
   
   for key, value in METHOD_INFO[method].items():
       print(f"{Fore.LIGHTYELLOW_EX + key} : {Fore.LIGHTGREEN_EX + value}")

def display_separator():
    console.print("_"*46, style="dim")

