"""This file creates csv files"""
import os
import csv

def export_problem_csv(current_problem):
    file_exists = os.path.exists("data/problems.csv") and os.path.getsize("data/problems.csv") > 0
    with open("data/problems.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=current_problem.keys())
        if not file_exists:
            writer.writeheader()      # Writes the keys
        writer.writerow(current_problem)

def export_txt(current_problem, solutions):
    for key, value in current_problem.items():
        format_c_p = f"{key} : {value}"
    for key, value in solutions.items():
        format_solutions  = f"{key} : {value}\n"

    with open("data/solutions.txt", "a") as file:
        file.write(f"Problem : {format_c_p}\nSolutions: {format_solutions}")

def export_json():
    pass

def save_history():
    pass