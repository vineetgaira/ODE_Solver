"""This file creates csv files"""
import os
import pandas as pd

def export_problme_csv(current_problem):

    df = pd.DataFrame([current_problem])

    file_exists = os.path.isfile("data/problems.csv")

    df.to_csv("data/problems.csv", mode="a", index = False, header=not file_exists)


def export_txt():
    pass

def export_json():
    pass

def save_history():
    pass