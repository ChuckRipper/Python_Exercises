class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __del__(self):
        print(f'"{self.imie}" "{self.nazwisko}" umiera')
