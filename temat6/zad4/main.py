from math import sqrt

def d(x, y, z=None):
    if z is None:
        return sqrt(x**2 + y**2)
    return sqrt(x**2 + y**2 + z**2)
