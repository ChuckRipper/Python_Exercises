import string

wejscie = input()
if any(char not in string.ascii_letters for char in wejscie):
    print("TAK")
else:
    print("NIE")
