class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Wektor(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Wektor(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
