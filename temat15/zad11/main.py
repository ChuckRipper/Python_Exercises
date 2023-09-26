import io
import logging

def wyjscie(func):
    def wrapper(*args, **kwargs):
        if not hasattr(func, 'logs'):
            func.logs = io.StringIO()
            logging.basicConfig(level=logging.INFO, stream=func.logs)
        try:
            result = func(*args, **kwargs)
            logging.info(f"Funkcja {func.__name__} wykonała się poprawnie.")
            return result
        except Exception as e:
            logging.error(f"Funkcja {func.__name__} wykonała się niepoprawnie.")
            raise e
    return wrapper
