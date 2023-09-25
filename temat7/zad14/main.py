# Wariant #1
# def roznica_wysokosci(a, wysokosc=None, glebokosc=None):
#     if wysokosc:
#         return a - wysokosc
#     elif glebokosc:
#         return glebokosc - a
#     return a

# for slownik in wejscie:
#     print(roznica_wysokosci(**slownik))

# Wariant #2
# def roznica_wysokosci(a, **kwargs):
#     if 'wysokosc' in kwargs:
#         return a - kwargs['wysokosc']
#     if 'glebokosc' in kwargs:
#         return kwargs['glebokosc'] - a
#     return a

# for slownik in wejscie:
#     print(roznica_wysokosci(**slownik))

# Wariant #3
def roznica_wysokosci(a, wysokosc=None, glebokosc=None):
    if wysokosc is not None:
        return a - wysokosc
    if glebokosc is not None:
        return glebokosc - a
    return a

for slownik in wejscie:
    print(roznica_wysokosci(**slownik))
