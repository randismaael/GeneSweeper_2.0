from Bio import Entrez 
from Bio import SeqIO

Entrez.email = "aalajlan6@gatech.edu"  # Change it to your email address
gene_id = "3300066319 assembled Ga0610651_106470_1_93"
handle = Entrez.efetch(db="protein", id=gene_id, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")  # Reading the sequence
handle.close()
print(gene_id, str(record.seq))  # Returns a tuple with the gene_id and the amino acid sequence