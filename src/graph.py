"""This file will store functions to plot a graph."""
import os
import re
import time
import matplotlib.pyplot as plt
from src.settings import get_setting

GRAPH_DIR = "data/graphs"

def _build_solution_plot(history, method_name, equation):

    x, y = zip(*history)
    if get_setting("graph_style") == "scatter":
        plt.scatter(x, y)
    else:
        plt.plot(x, y)
    plt.ylabel("Values of y")
    plt.title(f"{method_name.capitalize()}\ndy/dx = {equation}")
    plt.xlabel("Values of x")
    plt.show()

def _build_comparison_plot(solutions, equation):
    for method_name, history in solutions.items():
        x, y = zip(*history)
        if get_setting("graph_style") == "scatter":
            plt.scatter(x, y, label=method_name.capitalize())
        else:
            plt.plot(x, y, label=method_name.capitalize())
    plt.ylabel("Values of y")
    plt.xlabel("Values of x")
    plt.title(f"Method Comparison\ndy/dx = {equation}")
    plt.legend()
    plt.show()

def plot_solution(history, method_name, equation):
    _build_solution_plot(history, method_name, equation)
    plt.show()

def plot_comparison(solutions, equation):
    _build_comparison_plot(solutions, equation)
    plt.show()

def _slugify(text):
    text = str(text)
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")
    return text[:40]

def save_graph(last_plot):
    os.makedirs(GRAPH_DIR, exist_ok=True)

    if last_plot["type"] == "solution":
        _build_solution_plot(last_plot["history"], last_plot["method"], last_plot["equation"])
        name_part = f"{last_plot['method']}_{_slugify(last_plot['equation'])}"
    else:
        _build_comparison_plot(last_plot["solutions"], last_plot["equation"])
        name_part = f"comparison_{_slugify(last_plot['equation'])}"

    filename = f"{name_part}_{int(time.time())}.png"
    filepath = os.path.join(GRAPH_DIR, filename)
    plt.savefig(filepath)
    plt.close()
    return filepath