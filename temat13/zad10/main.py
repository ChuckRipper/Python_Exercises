class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self._oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def dodaj_ocene(self, ocena):
        if not (isinstance(ocena, int) and 1 <= ocena <= 6):
            raise ValueError("Nieprawidłowa ocena!")
        self._oceny.append(ocena)
        
    def __getitem__(self, index):
        return self._oceny[index]

    def __setitem__(self, index, value):
        if not (isinstance(value, int) and 1 <= value <= 6):
            raise ValueError("Nieprawidłowa ocena!")
        self._oceny[index] = value

    def __delitem__(self, index):
        del self._oceny[index]

    def __len__(self):
        return len(self._oceny)

    def __iter__(self):
        return iter(self._oceny)

    def __float__(self):
        if len(self._oceny) == 0:
            return 0.0
        return sum(self._oceny) / len(self._oceny)
