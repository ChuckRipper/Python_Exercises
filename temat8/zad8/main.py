def wiecej_wiecej(values):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for value in values:
                yield func(value, *args, **kwargs)
        return wrapper
    return decorator
