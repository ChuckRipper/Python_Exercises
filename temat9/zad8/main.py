# class Wejscie:
#     def __init__(self):
#         self._parametr = None

class Wyjscie(Wejscie):
    @property
    def parametr(self):
        return self._parametr

    @parametr.setter
    def parametr(self, value):
        print("Zamiana wartości")
        self._parametr = value

    @parametr.deleter
    def parametr(self):
        self._parametr = None