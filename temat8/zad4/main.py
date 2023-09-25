def obserwuj(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Wykorzystanie func.__name__ do przekazania komunikatu
        informacja = obserwatorzy.get(func.__name__)
        if informacja:
            for pani, value in informacja.items():
                if value:
                    globals()["informuj_" + pani](f"Funkcja {func.__name__} została wywołana o czasie {time()} i życzy smacznej kawusi")
        return result

    return wrapper
