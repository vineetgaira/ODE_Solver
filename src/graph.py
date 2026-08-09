"""This file will store functions to plot a graph."""
import matplotlib.pyplot as plt
from src.display import display_error

def plot_solution(history=None, method_name=None, equation=None):

    if history is not None:
        x, y = zip(*history)
        plt.plot(x, y)
        plt.ylabel("Values of y")
        plt.title(f"{method_name.capitalize()}\ndy/dx = {equation}")
        plt.xlabel("Values of x")
        plt.show()
    else:
        display_error("No solution to plot yet.")


def plot_comparison(solutions):
    
    for kye, value in solutions.items():
        x, y = zip(*value)
        plt.plot(x, y)
        plt.ylabel()


def plot_exact_solution(exact):
    pass

def save_graph():
    pass