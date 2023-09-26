import datetime

wyjscie = {}
for osoba1, (start1, dni1) in wejscie.items():
    wspolny_urlop = []
    koniec1 = start1 + datetime.timedelta(days=dni1)
    for osoba2, (start2, dni2) in wejscie.items():
        if osoba1 != osoba2:
            koniec2 = start2 + datetime.timedelta(days=dni2)
            if start1 <= koniec2 and koniec1 >= start2:
                wspolny_urlop.append(osoba2)
    wyjscie[osoba1] = wspolny_urlop
