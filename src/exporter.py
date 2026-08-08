"""This file creates csv files"""
import os
import csv
import json

CACHE_FILE = "data/problems.csv"

def export_problem_csv(current_problem):
    file_exists = os.path.exists(CACHE_FILE) and os.path.getsize(CACHE_FILE) > 0
    with open(CACHE_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=current_problem.keys())
        if not file_exists:
            writer.writeheader()      # Writes the keys
        writer.writerow(current_problem)

def export_txt(current_problem):

    for key , value in current_problem.items():
        with open ("data/problems.txt", "a") as file:
            file.write(f"{key} : {value} \n")

def json_serialized(equation, initial_x, initial_y, target_x, step_size, precision=6):

    return {
    "equation": str(equation),
    "x0": (round(initial_x, precision)),
    "y0": (round(initial_y, precision)),
    "target_x": (round(target_x, precision)),
    "step_size": (round(step_size, precision))
    }

def export_json(problem_record):

    path = "data/problems.json"
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(problem_record)

    with open(path, "w") as file:
        json.dump(data, file, sort_keys=True, indent=2)
    
def save_history(history):
    pass


