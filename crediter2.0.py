import glob
import os   

# Specify the folder path where your .txt files are located
folder_path = 'C:/Users/burak/Desktop/instaloader/babybearyuki'

# Use glob to get a list of all .txt files in the folder
txt_files = glob.glob(f"{folder_path}/*.txt")

# Loop through each .txt file and append text
folder_name= os.path.basename(folder_path)
text_to_append = "\n\nCredit: " + folder_name

for file_name in txt_files:
    with open(file_name, "a") as file:
        file.write(text_to_append + "\n")


