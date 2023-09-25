# Wariant #1
# def obserwuj(func):
#     from functools import wraps

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         # Wykorzystanie func.__name__ do przekazania komunikatu
#         informacja = obserwatorzy.get(func.__name__)
#         if informacja:
#             for pani, value in informacja.items():
#                 if value:
#                     globals()["informuj_" + pani](f"Funkcja {func.__name__} została wywołana o czasie {time()} i życzy smacznej kawusi")
#         return result

#     return wrapper

# Wariant #2
for planetoid in wejscie:
    def count_ref(position, data=planetoid):
        return count_refluxibility(*data.values(), position)
    planetoid["count_refluxibility"] = count_ref

wyjscie = wejscie
