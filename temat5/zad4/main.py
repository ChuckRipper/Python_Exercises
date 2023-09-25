with open("wejscie.txt", "r") as f:
    lines = f.readlines()

with open("wejscie.txt", "w") as f:
    for line in lines:
        if line.startswith("A"):
            f.write(line)
