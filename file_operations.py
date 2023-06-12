import csv

results = []
filename = 'note1.csv'
with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        results.append(row)
    print(results)
