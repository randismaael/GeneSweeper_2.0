from Bio import Entrez 
from Bio import SeqIO
Entrez.email = "omaralshamsi14@gmail.com"  # Change this to your actual email address
try:
    gene_id="3300002862 assembled Ga0004695J43176_1011036"
    handle = Entrez.efetch(db="protein", id=gene_id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    print(gene_id, str(record.seq)) 
except Exception as e:
    print( gene_id, f"Error: {e}")

# gets sequences and write them to a fasta file
def generate_fasta_file():
    csv_filename = "output_file.csv"
    fasta_filename = "amino_acid_sequences.fasta"

    log_text.delete(1.0, tk.END)

    if not os.path.exists(csv_filename):
        log_text.insert(tk.END, f"Error: {csv_filename} does not exist.\n")
        root.update_idletasks()
        return

    log_text.insert(tk.END, f"Reading gene IDs from {csv_filename}...\n")
    root.update_idletasks()

    gene_ids = []
    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)

        log_text.insert(tk.END, f"CSV Header: {header}\n")

        for row in csv_reader:
            log_text.insert(tk.END, f"Processing row: {row}\n")
            if len(row) >= 4:  # Assuming the gene ID is in the fourth column (index 3)
                gene_id = row[3]  # Modify this index based on the actual structure
                if gene_id.strip():  # Check if gene_id is not empty or just whitespace
                    gene_ids.append(gene_id)
                else:
                    log_text.insert(tk.END, f"Skipping row with empty gene ID: {row}\n")
            else:
                log_text.insert(tk.END, f"Skipping row with insufficient columns: {row}\n")

    if not gene_ids:
        log_text.insert(tk.END, "No gene IDs found. Ensure the input file has the correct data.\n")
        root.update_idletasks()
        return

    log_text.insert(tk.END, f"Found {len(gene_ids)} gene IDs.\n")
    root.update_idletasks()

    log_text.insert(tk.END, f"Generating FASTA file: {fasta_filename}\n")
    root.update_idletasks()

    with open(fasta_filename, "w") as fasta_file:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_gene_id = {executor.submit(fetch_amino_acid_sequence, gene_id): gene_id for gene_id in gene_ids}
            
            for future in concurrent.futures.as_completed(future_to_gene_id):
                gene_id = future_to_gene_id[future]
                try:
                    gene_id, sequence = future.result()
                    if "Error:" in sequence:
                        log_text.insert(tk.END, f"Error fetching sequence for {gene_id}: {sequence}\n")
                    else:
                        if sequence:
                            fasta_file.write(f">{gene_id}\n{sequence}\n")
                            log_text.insert(tk.END, f"Successfully fetched sequence for {gene_id}\n")
                        else:
                            log_text.insert(tk.END, f"No sequence returned for {gene_id}\n")
                except Exception as e:
                    log_text.insert(tk.END, f"Error processing sequence for {gene_id}: {e}\n")
                root.update_idletasks()

    log_text.insert(tk.END, "FASTA file generation complete.\n")
    root.update_idletasks()