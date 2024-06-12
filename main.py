import pandas as pd
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
folder_name = 'CSV files'
csv_folder_path = os.path.join(current_directory, folder_name)
def iterate_csv_files():
    for filename in os.listdir(folder_name):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_folder_path, filename)
            with open(file_path, "r") as file:
                db = pd.read_csv(file, sep='delimiter', header=None, engine='python')