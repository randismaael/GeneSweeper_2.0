######### NOT DEBUGGED PLEASE LEAVE FOR NOW

//imported pandas and tkinter

def copy_and_rename_files(product):
    folder_path = os.path.dirname(os.path.realpath(__file__))
    original_file = os.path.join(folder_path, "output_file.csv")
    product_file = os.path.join(folder_path, f"{product}_output.csv")
    link_output_file = os.path.join(folder_path, "Link_Output.csv")
    renamed_link_output_file = os.path.join(folder_path, f"{product}_Link_Output.csv")
    
    # Initialize tkinter elements (for logging)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    log_text = tk.Text(root)
    log_text.pack()
    
    def log_message(message):
        log_text.insert(tk.END, message + '\n')
        root.update_idletasks()

    # Copy and rename the original file
    try:
        df = pd.read_csv(original_file)
        df.to_csv(product_file, index=False)
        log_message(f"Copied and renamed to {product_file}.")
    except FileNotFoundError:
        log_message(f"Error: {original_file} does not exist.")
    
    # Copy and rename the Link_Output file
    try:
        df_link = pd.read_csv(link_output_file)
        df_link.to_csv(renamed_link_output_file, index=False)
        log_message(f"Copied and renamed to {renamed_link_output_file}.")
    except FileNotFoundError:
        log_message(f"Error: {link_output_file} does not exist.")



def filter_and_append_to_csv(input_file, output_file, product):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Filter the DataFrame based on the product name
    filtered_df = df[df['Product'].str.contains(product, na=False)]

    # Append to the output CSV file
    filtered_df.to_csv(output_file, mode='a', index=False, header=not pd.read_csv(output_file).empty)

    log_text.insert(tk.END, f"Filtered and appended data to {output_file}.\n")
    root.update_idletasks()

# Example of initializing tkinter elements
root = tk.Tk()
log_text = tk.Text(root)
log_text.pack()

# Example usage
filter_and_append_to_csv('input.csv', 'output.csv', 'ProductA')

root.mainloop()

    
    root.mainloop()

# Example usage
copy_and_rename_files('example_product')
