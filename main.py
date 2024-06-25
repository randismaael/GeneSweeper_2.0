import os
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox
import shutil  # for copying files
import concurrent.futures  # for asynchronously executing
from Bio import Entrez
from Bio import SeqIO

# Set your email for Entrez
Entrez.email = "yourEmail@gmail.com"

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_name = 'CSV files'
csv_folder_path = os.path.join(current_directory, folder_name)

def iterate_csv_files():
    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_folder_path, filename)
            with open(file_path, "r") as file:
                db = pd.read_csv(file, delimiter="\t", header=None, engine='python')
                # Process db......
                #logic as needed
                
#did not change this function since it is related to file handling and has nothing to do with pandas
def enum():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    log_text.insert(tk.END, "Enumerating files...\n")
    root.update_idletasks()
    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(csv_folder_path) if file.startswith('rnaseq_data')]
    # Rename each file with a numbered format
    for index, file in enumerate(csv_files, start=1):
        old_path = os.path.join(csv_folder_path, file)
        new_name = f"{index}.csv"
        new_path = os.path.join(csv_folder_path, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            
    log_text.insert(tk.END, "Files have been successfully renamed.\n")
    root.update_idletasks()

#optimized using pandas
def filter_and_append_to_csv(input_file, output_file, product):
    try:
        df_input = pd.read_csv(input_file)
        filtered_df = df_input[df_input.iloc[:, 0].str.contains(product, na=False)]
        
        if not os.path.exists(output_file):
            filtered_df.to_csv(output_file, index=False)
        else:
            filtered_df.to_csv(output_file, mode='a', header=False, index=False)

        log_text.insert(tk.END, f"Filtered and appended data to {output_file}.\n")
    except Exception as e:
        log_text.insert(tk.END, f"Error processing {input_file}: {str(e)}\n")
        
    root.update_idletasks()
#optimized using pandas
def linkgen():
    try:
        filename = "output_file.csv"
        df = pd.read_csv(filename)
        df['Link'] = df.apply(lambda row: f"https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaGeneDetail&page=genePageMainFaa&taxon_oid={row[0]}&data_type=assembled&gene_oid={row[2].split(',')[0]}", axis=1)
        link_df = df[['Gene seq length', 'Link']]
        link_df.to_csv("Link_Output.csv", index=False)
        log_text.insert(tk.END, "Done generating links.\n")
    except Exception as e:
        log_text.insert(tk.END, f"Error generating links: {str(e)}\n")
    root.update_idletasks()
#optimized using pandas
def delete_csv_files():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    csv_files = [file for file in os.listdir(folder_path) if has_numbers(file) and file.endswith('.csv')]
    deleted_files_df = pd.DataFrame(columns=['Filename'])

    for file in csv_files:
        os.remove(os.path.join(folder_path, file))
        deleted_files_df = deleted_files_df.append({'Filename': file}, ignore_index=True)

    log_text.insert(tk.END, "CSV files have been deleted.\n")
    root.update_idletasks()
    
#not changed
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

# Initialize Tkinter root and log_text
root = tk.Tk()
log_text = tk.Text(root)
log_text.pack()

root.mainloop()

