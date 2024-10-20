import numpy as np
import pandas as pd
import json

# csv file

path = r'D:\BSAI 3rd Semester\ML course\industry.csv'

df = pd.read_csv(path)

df

print(df)

# json file

path = r'D:\BSAI 3rd Semester\\ML course\json file.json'

with open (path, 'r') as json_file:
    df = json.load(json_file)

df

#text file

file_path = r'D:\BSAI 3rd Semester\ML course\text file.txt'

with open (file_path, 'r') as text_file:
    df = text_file.read()


# excel file

file_path = r'D:\BSAI 3rd Semester\ML course\excel file.xlsx'

df = pd.read_excel(file_path)


# Function to display file options and get user's choice
def options():
    # Display the list of file types that can be uploaded
    print("List of files that you can upload")
    print("1. CSV")  # Option for CSV files
    print("2. JSON")  # Option for JSON files
    print("3. TXT")  # Option for text files
    print("4. XLSX")  # Option for Excel files

    # Return the user's input as an integer (indicating their file choice)
    return int(input("Enter which file you want to upload: "))

# Function to load the file based on user's input
def load_file():
    # Get the file type chosen by the user (1 for CSV, 2 for JSON, etc.)
    file_type = options()

    # Prompt the user to input the full file path
    file_path = input(f"Enter the complete path of file with file name and type : ")

    # Based on the file type, load the corresponding file
    if file_type == 1:
        # If CSV, use pandas to read CSV into a DataFrame
        df = pd.read_csv(file_path)
    elif file_type == 2:
        # If JSON, open the file and load its contents into a dictionary
        with open(file_path, 'r') as json_file:
            df = json.load(json_file)
    elif file_type == 3:
        # If text file, open and read the entire file into a string
        with open(file_path, 'r') as text_file:
            df = text_file.read()
    elif file_type == 4:
        # If Excel file, use pandas to read Excel into a DataFrame
        df = pd.read_excel(file_path)
    else:
        # If the user inputs an invalid file type, return an error message
        return "The File Type is not supported in this code"

    # Return the loaded data (whether DataFrame, JSON object, or text)
    return df

# Call the function to load the file and store the result in a variable
dataframe = load_file()

# Output the loaded data to check if it's loaded correctly
dataframe
