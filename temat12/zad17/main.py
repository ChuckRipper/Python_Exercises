from fractions import Fraction

sum = Fraction(1)
term = Fraction(1)
for i in range(1, n):
    term *= Fraction(x, i)
    sum += term
wynik = sum
