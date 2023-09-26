import datetime

dni_tygodnia = {
    0: "PONIEDZIAŁEK",
    1: "WTOREK",
    2: "ŚRODA",
    3: "CZWARTEK",
    4: "PIĄTEK",
    5: "SOBOTA",
    6: "NIEDZIELA"
}

dzisiaj = datetime.datetime.now().weekday()
print(dni_tygodnia[dzisiaj])
