import os

if not os.path.exists('dzienniki'):
    os.mkdir('dzienniki')

for _ in range(10):
    imie = input().strip()
    with open(os.path.join('dzienniki', f"{imie}.txt"), 'w') as f:
        pass
