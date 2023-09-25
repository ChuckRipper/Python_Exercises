with open("wejscie.txt", "r") as f:
    content = f.read()

with open("wyjscie.txt", "w") as f:
    f.write(content[::-1])
