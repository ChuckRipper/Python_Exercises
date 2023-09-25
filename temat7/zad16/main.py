def odwrotny_sumator(*args):
    return sum(1/arg for arg in args if arg != 0)

for lista in wejscie:
    print(odwrotny_sumator(*lista))
