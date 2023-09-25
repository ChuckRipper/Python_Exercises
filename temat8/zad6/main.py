# Wariant #1
# def stringer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return str(func(*args, **kwargs))
#     return wrapper

# Wariant #2
def stringer(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))
    return wrapper
