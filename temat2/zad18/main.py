suma = 0
iloczyn = 1
ilosc = 0
while True:
    liczba = float(input())
    if liczba <= 0:
        break
    suma += liczba
    iloczyn *= liczba
    ilosc += 1
print(suma)
print(iloczyn)
print(suma/ilosc)
print(iloczyn**(1/float(ilosc)))
