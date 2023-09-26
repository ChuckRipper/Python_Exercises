class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
