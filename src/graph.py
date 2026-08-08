"""This file will store functions to plot a graph."""
import matplotlib.pyplot as plt
from src.display import display_error

def plot_solution(history, method_name, equation):

    if history is not None:
        x, y = zip(*history)
        plt.plot(x, y)
        plt.ylabel("Values of y")
        plt.title(f"{method_name.capitalize()}\n{equation}")
        plt.xlabel("Values of x")
        plt.show()
    else:
        display_error("Please enter a equation and solve with a method first.")


def plot_comparison(solutions):
    pass

def plot_exact_solution(exact):
    pass

def save_graph():
    pass