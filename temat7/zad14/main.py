def roznica_wysokosci(a, wysokosc=None, glebokosc=None):
    if wysokosc:
        return a - wysokosc
    elif glebokosc:
        return glebokosc - a
    return a

for slownik in wejscie:
    print(roznica_wysokosci(**slownik))
