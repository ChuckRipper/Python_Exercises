import functools

def suma(a, b):
    if isinstance(a, (list, tuple, set)):
        return type(a)(a) + type(b)(b)
    elif isinstance(a, dict):
        return {**a, **b}

    raise ValueError("Unsupported data type")

# For extending functionality:
def suma_for_new_type(a, b, result_type):
    functools.partial(suma, a=a, b=b, result_type=result_type)
