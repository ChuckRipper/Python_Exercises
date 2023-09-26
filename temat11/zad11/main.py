import string
import random

text = input()
letters = string.ascii_letters
shuffled = random.sample(letters, len(letters))
mapping = str.maketrans(letters, ''.join(shuffled))
print(text.translate(mapping))
