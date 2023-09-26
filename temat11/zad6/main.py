import re

value = input()
if re.match("^\d+$", value):
    print("LICZBA")
else:
    print("NIELICZBA")
