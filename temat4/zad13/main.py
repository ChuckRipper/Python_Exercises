import string

wejscie = input()
if any(char in string.whitespace for char in wejscie):
    print("TAK")
else:
    print("NIE")
