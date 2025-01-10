import csv

path : str = 'example.csv'

file_csv: list = []
with open(file=path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        file_csv.append(row)

print(file_csv)