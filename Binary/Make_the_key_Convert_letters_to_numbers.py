import random
from pickle import dump
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYX"

r1=list(letters)
random.shuffle(r1)
#r1="".join(r1)
print(r1)
index_letters=r1.index("q")

f=open("Binary/password/key.letter","wb")
dump((r1),f)
f.close()
print(index_letters)