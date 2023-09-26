import calendar

kalendarz = calendar.monthcalendar(datetime.datetime.now().year, datetime.datetime.now().month)
for tydzien in kalendarz:
    wiersz = []
    for dzien in tydzien:
        if dzien == 0:
            wiersz.append("[  ]")
        else:
            wiersz.append(f"[{dzien:02}]")
    print(' '.join(wiersz))
