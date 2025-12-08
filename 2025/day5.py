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
    ranges[i] = [int(low), int(high)]

ids = [int(x) for x in ids]

def part_one():
    valid = 0

    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                valid += 1
                break

    print(valid)

#601 part1 answer

    

def part_two():
    ranges.sort(key=lambda x: x[0])
    
    merged = []
    for range in ranges:
        #if nothing in list yet OR starts after last finishes
        if not merged or range[0] > merged[-1][1]:
            merged.append(range)
        #else, there is an overlap.
        else:
            #set high on last interval to the max of last and current
            merged[-1][1] = max(merged[-1][1], range[1])
    

    total_ids = 0
    for low, high in merged:
        total_ids += high - low + 1
    print(total_ids)



part_two()

#367899984917516 part2 answer