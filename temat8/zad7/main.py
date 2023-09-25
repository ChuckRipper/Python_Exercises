# Wariant #1
# def bezbledny(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception:
#             print(f"Funkcja {func.__name__} wywołała błąd, ale jest jej bardzo przykro")
#     return wrapper

# Wariant #2
def bezbledny(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            print(f"Funkcja {func.__name__} wywołała błąd, ale jest jej bardzo przykro")
    return wrapper
