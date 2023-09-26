# Wariant #1
# unikalne_wartosci = set(val for tuple_vals in wejscie.values() for val in tuple_vals)
# for wartosc in unikalne_wartosci:
#     print(wartosc)

# Wariant #2
unikalne_wartosci = set()
for tuple_vals in wejscie.values():
    unikalne_wartosci.update(tuple_vals)
for wartosc in unikalne_wartosci:
    print(wartosc)
