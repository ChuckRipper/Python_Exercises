from decimal import Decimal, getcontext

getcontext().prec = precision
wynik = [Decimal(x).ln() for x in numbers]
