wyjscie = {}
for nr, przedmioty in wejscie.items():
    srednia = sum(sum(oceny) for oceny in przedmioty.values()) / sum(len(oceny) for oceny in przedmioty.values())
    wyjscie[nr] = srednia
