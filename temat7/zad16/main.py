# Wariant #1
# def odwrotny_sumator(*args):
#     return sum(1/arg for arg in args if arg != 0)

# for lista in wejscie:
#     print(odwrotny_sumator(*lista))

# Wariant #2
def odwrotny_sumator(*args):
    return sum([1/int(arg) for arg in args if arg != 0])

for lista in wejscie:
    print(odwrotny_sumator(*lista))

# Wariant #3
# def odwrotny_sumator(*args):
#     suma = 0
#     for arg in args:
#         if arg:
#             suma += 1/arg
#     return suma

# for lista in wejscie:
#     print(odwrotny_sumator(*lista))
