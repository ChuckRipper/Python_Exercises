import datetime

def odliczanie(data):
    # Algorytm do obliczenia daty Wielkanocy dla kalendarza Julian
    a = data.year % 4
    b = data.year % 7
    c = data.year % 19
    d = (19*c + 15) % 30
    e = (2*a + 4*b - d + 34) % 7
    month = (d + e + 114) // 31
    day = ((d + e + 114) % 31) + 1
    wielkanoc_julian = datetime.date(data.year, month, day)

    # Korekta dla kalendarza gregoriańskiego
    korekta = (data.year // 100) - (data.year // 400) - 2
    wielkanoc_gregorianska = wielkanoc_julian + datetime.timedelta(days=korekta)

    roznica = wielkanoc_gregorianska - data
    return roznica.days
