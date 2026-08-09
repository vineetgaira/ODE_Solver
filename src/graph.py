"""This file will store functions to plot a graph."""
import matplotlib.pyplot as plt
from src.display import display_error
from src.settings import get_setting

def plot_solution(history, method_name, equation):

    x, y = zip(*history)
    if get_setting("graph_style") == "scatter":
        plt.scatter(x, y)
    else:
        plt.plot(x, y)
    plt.ylabel("Values of y")
    plt.title(f"{method_name.capitalize()}\ndy/dx = {equation}")
    plt.xlabel("Values of x")
    plt.show()

def plot_comparison(solutions):

    for kye, value in solutions.items():
        x, y = zip(*value)
        plt.plot(x, y)
        plt.ylabel()


def plot_exact_solution(exact):
    pass

def save_graph():
    pass