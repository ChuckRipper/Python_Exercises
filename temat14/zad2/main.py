import csv

with open('wejscie.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        values = [float(x) for x in row]
        print(sum(values) / len(values))
