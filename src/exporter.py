"""This file creates csv files"""
import os
import csv

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
            file.write(f"{key} : {value}, ")


def export_json():
    pass

def save_history():
    pass