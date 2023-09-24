liczba_parzystych = 0
while True:
    dane = input()
    if dane == "STOP":
        break
    if int(dane) % 2 == 0:
        liczba_parzystych += 1
print(liczba_parzystych)
