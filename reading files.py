import numpy as np
import pandas as pd
import json

# path = r'D:\BSAI 3rd Semester\ML course\industry.csv'

# df = pd.read_csv(path)

# df

# print(df)

# json file

# path = r'D:\BSAI 3rd Semester\\ML course\json file.json'

# with open (path, 'r') as json_file:
#     df = json.load(json_file)

# df

#text file

# file_path = r'D:\BSAI 3rd Semester\ML course\text file.txt'

# with open (file_path, 'r') as text_file:
#     df = text_file.read()


# excel file

file_path = r'D:\BSAI 3rd Semester\ML course\excel file.xlsx'

df = pd.read_excel(file_path)