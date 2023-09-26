from functools import partialmethod

class Wyjscie(Wejscie):
    def __init__(self, dic):
        for key, value in dic.items():
            setattr(self, f"metoda_{key}", partialmethod(self.metoda, value))
