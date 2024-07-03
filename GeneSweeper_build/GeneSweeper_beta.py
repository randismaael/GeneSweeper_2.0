import pandas as pd
csvFile = open("test_file.csv", "r")
df = pd.read_csv(csvFile, delimiter="\t")
print(df.info())