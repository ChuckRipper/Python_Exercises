def przywitanie_funkcji(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Funkcja {func.__name__} czuje się kochana")
        return func(*args, **kwargs)
    return wrapper
