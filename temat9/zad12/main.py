class Akolita:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.zostal_poswiecony = False

    def zabij(self):
        if not self.zostal_poswiecony:
            print(f"Akolita {self.imie} {self.nazwisko} zostaje poświęcony wyższej sprawie")
            self.zostal_poswiecony = True
        else:
            print("Śniący rozgniewał się, ponieważ ofiarowano mu zwłoki")

class Kaplan:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ofiary = []

    def zabij(self, akolita):
        akolita.zabij()
        if akolita.zostal_poswiecony:
            self.ofiary.append(f"{akolita.imie} {akolita.nazwisko}")

    def wspomnij(self):
        print(f"Wspomnij, o Śniący, na ofiarowanych ci akolitów: {', '.join(self.ofiary)}")

class Arcykaplan(Kaplan):
    def zanies_modly(self, *prosby):
        for prosba in prosby:
            print(prosba)

    @staticmethod
    def awansuj(kaplan):
        return Arcykaplan(kaplan.imie, kaplan.nazwisko)