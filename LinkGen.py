
import csv
filename = "18.1.2024_output_file.csv"
f = open(filename, "r")
header = f.readline().strip().split() #Header to ignore
lines = f.readlines() #Get all lines (Besides header)
f.close()

with open("Link_Output.csv", "a", newline='') as o:
    csv_writer = csv.writer(o)
    for line in lines:
        line = line.strip().split()
        link = "https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaGeneDetail&page=genePageMainFaa&taxon_oid=" + line[0] + "&data_type=assembled&gene_oid=" + line[2]
        csv_writer.writerow([link])

