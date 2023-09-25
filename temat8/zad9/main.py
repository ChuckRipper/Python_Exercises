def obserwuj(func):
    from functools import wraps
    from time import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        obserwacje = obserwatorzy.get(func.__name__, {})
        komunikat = f"Funkcja {func.__name__} została wywołana o czasie {time()} i życzy smacznej kawusi"

        if "anetke" in obserwacje and obserwacje["anetke"]:
            informuj_anetke(komunikat)
        if "beatke" in obserwacje and obserwacje["beatke"]:
            informuj_beatke(komunikat)
        if "czeske" in obserwacje and obserwacje["czeske"]:
            informuj_czeske(komunikat)
        if "danke" in obserwacje and obserwacje["danke"]:
            informuj_danke(komunikat)
        if "elke" in obserwacje and obserwacje["elke"]:
            informuj_elke(komunikat)

        return result

    return wrapper
