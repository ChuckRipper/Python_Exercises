from fractions import Fraction

wynik = Fraction(len(numbers)) / sum(Fraction(1, x) for x in numbers)
