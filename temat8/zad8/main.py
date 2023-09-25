# Wariant #1
# def wiecej_wiecej(values):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for value in values:
#                 yield func(value, *args, **kwargs)
#         return wrapper
#     return decorator

# Wariant #2
def wiecej_wiecej(list_values):
    def decorator(func):
        def generator_wrapper(*args, **kwargs):
            for value in list_values:
                yield func(value, *args, **kwargs)
        return generator_wrapper
    return decorator
