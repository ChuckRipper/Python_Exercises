def bin_to_dec(*args):
    return sum(2**i * arg for i, arg in enumerate(args))
