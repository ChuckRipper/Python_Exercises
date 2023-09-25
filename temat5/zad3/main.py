with open("wejscie.txt", "r") as f:
    numbers = f.readlines()
    total = sum([int(num.strip()) for num in numbers])
    print(total)
