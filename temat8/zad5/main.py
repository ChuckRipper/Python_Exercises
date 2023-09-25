# Wariant #1
# def przywitanie_funkcji(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Funkcja {func.__name__} czuje się kochana")
#         return func(*args, **kwargs)
#     return wrapper

# Wariant #2
def przywitanie_funkcji(func):
    def wrapper(*args, **kwargs):
        print(f"Funkcja {func.__name__} czuje się kochana")
        return func(*args, **kwargs)
    return wrapper
