import re

text = input()
match = re.search(wejscie, text)
print(match.start() if match else "Brak dopasowania")
