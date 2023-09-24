n = int(input())
while n > 1:
    if n % 2:
        print("NIE")
        break
    n //= 2
else:
    print("TAK")
