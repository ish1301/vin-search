import csv

csv.register_dialect("piper", delimiter="|", quoting=csv.QUOTE_NONE)

# Path to inventory listing dump file text version
file_path = "./data/inventory-listing-2022-08-17.txt"

with open(file_path) as csvfile:
    for row in csv.DictReader(csvfile, dialect="piper"):
        print(row)
        exit()
