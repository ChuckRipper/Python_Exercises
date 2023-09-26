import csv

with open('wyjscie.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=wejscie[0].keys())
    writer.writeheader()
    for row in wejscie:
        writer.writerow(row)
