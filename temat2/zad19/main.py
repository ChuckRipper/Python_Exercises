a, b, c = float(input()), float(input()), float(input())
delta = b**2 - 4*a*c
if delta < 0:
    x1 = x2 = None
elif delta == 0:
    x1 = -b / (2*a)
    x2 = None
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
