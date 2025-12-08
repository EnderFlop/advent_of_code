import re
import itertools
import numpy as np
import time

#instructions = open("2025/day6testinput.txt").read().splitlines()
instructions = open("2025/day6input.txt").read().splitlines()

#organize input
problems = [[] for n in range(len(instructions[0].split()))]
for row in instructions[:-1]:
    row = row.split()
    for index, n in enumerate(row):
        problems[index].append(int(n))

total = 0

#run math
for index, symbol in enumerate(instructions[-1].split()):
    if symbol == "*":
        value = 1
        for n in problems[index]:
            value *= n
        
    elif symbol == "+":
        value = sum(problems[index])
    
    print(value)
    total += value

print(total)

#4580995422905 part1 answer