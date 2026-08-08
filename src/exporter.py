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
    "x0": str(round(initial_x, precision)),
    "y0": str(round(initial_y, precision)),
    "target_x": str(round(target_x, precision)),
    "step_size": str(round(step_size, precision))
    }


def export_json(problem_record):
    with open ("data/problems.json", "a") as file:
        json.dump(problem_record, file, sort_keys=True, indent=2)
    
def save_history():
    pass


