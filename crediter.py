import glob

# Specify the folder path where your .txt files are located
folder_path = 'C:/Users/burak/Desktop/crediter'

# Use glob to get a list of all .txt files in the folder
txt_files = glob.glob(f"{folder_path}/*.txt")

# Loop through each .txt file and append text
text_to_append = "\n\nCredit: " + "Bonbon"

for file_name in txt_files:
    with open(file_name, "a") as file:
        file.write(text_to_append + "\n")