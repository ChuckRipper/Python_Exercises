# Wariant #1
# def bin_to_dec(*args):
#     return sum(2**i * arg for i, arg in enumerate(args))

# Wariant #2
# def bin_to_dec(*bits):
#     return sum(bit << i for i, bit in enumerate(bits))

# Wariant #3
def bin_to_dec(*args):
    return sum([2**i for i, arg in enumerate(args) if arg == 1])
