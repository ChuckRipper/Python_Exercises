import io

wyjscie = io.StringIO()
for _ in range(10):
    imie = input()
    wyjscie.write(imie + '\n')
