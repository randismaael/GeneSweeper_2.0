import pandas as pd
csvFile = open("test_file.csv", "r")
db = pd.read_csv(csvFile, delimiter="\t")
print(db.info())
