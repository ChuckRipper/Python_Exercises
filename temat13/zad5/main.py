import datetime

def wiek(rok, miesiac, dzien, godzina=0, minuta=0, sekunda=0):
    teraz = datetime.datetime.now()
    urodziny = datetime.datetime(rok, miesiac, dzien, godzina, minuta, sekunda)
    roznica = teraz - urodziny

    lata = roznica.days // 365
    dni = roznica.days % 365
    godziny = roznica.seconds // 3600
    minuty = (roznica.seconds % 3600) // 60
    sekundy = roznica.seconds % 60

    return (lata, dni, godziny, minuty, sekundy)
