# Wariant #1
# unikalne_wartosci = set(val for list_vals in wejscie.values() for val in list_vals)
# for wartosc in unikalne_wartosci:
#     print(wartosc)

# Wariant #2
unikalne_wartosci = set()
for list_vals in wejscie.values():
    unikalne_wartosci.update(list_vals)
for wartosc in unikalne_wartosci:
    print(wartosc)
