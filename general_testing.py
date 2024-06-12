import pandas as pd
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
folder_name = 'CSV files'
csv_folder_path = os.path.join(current_directory, folder_name)
for filename in os.listdir(folder_name):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_folder_path, filename)
        print(filename)
        with open(file_path, "r") as file:
            # code goes below for each file
            print(file.readline())
            db = pd.read_csv(file_path, header=0, engine='python', delimiter='\t')
            print(db.columns)