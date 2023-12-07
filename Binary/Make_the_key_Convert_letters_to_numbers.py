import random
from pickle import dump

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYX"

r1 = list(letters)

random.shuffle(r1)

f = open("Binary/password/key.letter", "wb")
dump((r1), f)
f.close()
