import calendar

def xxi_wiek(dzien_tygodnia, dzien_miesiaca, numer_miesiaca):
    lata = []
    for rok in range(2001, 2101):
        if calendar.weekday(rok, numer_miesiaca, dzien_miesiaca) == dzien_tygodnia:
            lata.append(rok)
    return lata
