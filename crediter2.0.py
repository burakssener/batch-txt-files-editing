import os
from pathlib import Path

def append_credit_to_txt_files(folder_path):
    # Get all .txt files recursively in the specified folder
    txt_files = list(Path(folder_path).rglob("*.txt"))

    # Extract the folder name for credit
    folder_name = os.path.basename(folder_path)
    credit_text = "\n\nCredit: " + folder_name

    for file_path in txt_files:
        try:
            # Check if the credit text already exists in the file
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if credit_text not in content:
                    # Append the credit text to the file
                    with open(file_path, "a", encoding="utf-8") as file:
                        file.write(credit_text + "\n")
        except UnicodeDecodeError:
            print(f"Error reading file: {file_path}. Skipping.")

# Specify the folder path where your .txt files are located
folder_path = 'C:/Users/burak/Desktop/crediter'

# Call the function to append credit to all .txt files in subdirectories
append_credit_to_txt_files(folder_path)
