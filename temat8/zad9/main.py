# Wariant #1
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# wyjscie = fibonacci()

# Wariant #2
# def fibonacci():
#     yield 0
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a+b

# wyjscie = fibonacci()

# Wariant #3
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + a

wyjscie = fibonacci()
