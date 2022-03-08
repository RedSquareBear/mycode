#!/usr/bin/env python3

animallist = ["dog", "cat", "frog", "fox", "bee", "fly",]

print(animallist[0], animallist[1], animallist[2], animallist[3], animallist[4], animallist[5], sep = ", ")

i = 0

while (i < len(animallist)):
    print(animallist[i])
    i += 1
