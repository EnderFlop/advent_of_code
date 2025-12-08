import re
import itertools
import numpy as np
import time

#instructions = open("2025/day5testinput.txt").read().splitlines()
instructions = open("2025/day5input.txt").read().splitlines()

ranges = []
ids = []

#seperate instructions
after_split = False
for i in instructions:
    if i == "":
        after_split = True
        continue
    
    if not after_split:
        ranges.append(i)
    if after_split:
        ids.append(i)

#sanatize instructions
for i in range(len(ranges)):
    low, high = ranges[i].split("-")
    ranges[i] = (int(low), int(high))

ids = [int(x) for x in ids]

valid = 0

for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            valid += 1
            break

print(valid)

#601 part1 answer