from Bio import Entrez 
from Bio import SeqIO

Entrez.email = "aalajlan6@gatech.edu"  # Change it to your email address
handle = Entrez.efetch(db="protein", id=gene_id, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")  # Reading the sequence
handle.close()
return gene_id, str(record.seq)  # Returns a tuple with the gene_id and the amino acid sequence