import csv

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

file_path = ''

with open(file_path, "rb") as csvfile:
    for row in csv.DictReader(csvfile, dialect='piper'):
        print(row)
