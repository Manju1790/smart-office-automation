import os
import shutil
import pandas as pd
from report_generator import create_report
from email_sender import send_email

# ===============================
# Folder Configuration
# ===============================

INPUT_FOLDER = "input_files"
OUTPUT_FOLDER = "reports"
PROCESSED_FOLDER = "processed_files"

# Create all required folders automatically
for folder in [INPUT_FOLDER, OUTPUT_FOLDER, PROCESSED_FOLDER]:
    os.makedirs(folder, exist_ok=True)


# ===============================
# Get Files From Input Folder
# ===============================

def get_new_files():
    return os.listdir(INPUT_FOLDER)


# ===============================
# Process Each File
# ===============================

def process_file(file_name):
    file_path = os.path.join(INPUT_FOLDER, file_name)

    # Safety check
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        if "Amount" not in df.columns:
            print(f"'Amount' column missing in {file_name}")
            return

        total = df["Amount"].sum()
        average = df["Amount"].mean()

        # Generate PDF report
        report_path = create_report(file_name, total, average)

        # Send email
        send_email(report_path)

        # Move processed file
        shutil.move(file_path, os.path.join(PROCESSED_FOLDER, file_name))

        print(f"{file_name} processed successfully!")

    except Exception as e:
        print(f"Error processing {file_name}:", e)


# ===============================
# Main Runner
# ===============================

def run_system():
    files = get_new_files()

    if not files:
        print("No files found in input folder.")
        return

    for file in files:
        process_file(file)


#if __name__ == "__main__":
    #run_system()