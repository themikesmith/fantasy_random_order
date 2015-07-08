from random import shuffle
from sys import stdin

things_to_shuffle = []

for line in stdin:
    things_to_shuffle.append(line.strip())

shuffle(things_to_shuffle)
for index, thing in enumerate(things_to_shuffle):
    print index+1, thing
