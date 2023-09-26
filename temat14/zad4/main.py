import json

with open('wejscie.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    for entry in data:
        print(' '.join(entry.keys()))
