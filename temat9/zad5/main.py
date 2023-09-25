class Ocena:
    def __init__(self):
        self._wartosc = None

    @property
    def wartosc(self):
        return self._wartosc

    @wartosc.setter
    def wartosc(self, value):
        if value in [2, 3, 4, 5]:
            self._wartosc = value