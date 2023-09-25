def dzielniki(a):
    while a > 1:
        yield a % 2
        a //= 2
