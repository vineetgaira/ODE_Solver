"""This file creates csv files"""
import csv

def export_problem_csv(current_problem):
    with open("data/problems.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=current_problem.keys())

        writer.writeheader()      # Writes the keys
        writer.writerow(current_problem)

def export_txt():
    pass

def export_json():
    pass

def save_history():
    pass