# Wariant #1
# def powitanie(imie, nazwisko):
#     print(f"Witaj, {imie} {nazwisko}!")

# powitanie(imie=imie, nazwisko=nazwisko)

# Wariant #2
def powitanie(**kwargs):
    print(f"Witaj, {kwargs['imie']} {kwargs['nazwisko']}!")

powitanie(imie=imie, nazwisko=nazwisko)
