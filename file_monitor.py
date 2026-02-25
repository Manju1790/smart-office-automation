import os

INPUT_FOLDER = "input_files"

def get_new_files():
    files = os.listdir(INPUT_FOLDER)
    excel_files = [f for f in files if f.endswith(".xlsx")]
    return excel_files