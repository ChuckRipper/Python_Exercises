def only_strs(*args):
    for arg in args:
        yield from (str(x) for x in arg)
