import re
import itertools
import numpy as np
import time

#instructions = open("2025/day6testinput.txt").read().splitlines()
instructions = open("2025/day6input.txt").read().splitlines()

#organize input
problems = [[] for n in range(len(instructions[0].split()))]

# part1 number reading

# for row in instructions[:-1]:
#     row = row.split()
#     for index, n in enumerate(row):
#         problems[index].append(int(n))

# part2 number reading

col_idx = len(instructions[0]) - 1
problem_idx = len(problems) - 1
while col_idx >= 0:
    current_num = []
    for row in instructions[:-1]:
        current_num.append(row[col_idx])
    #if all blanks, we are in the space between nums
    if all(elem == " " for elem in current_num):
        problem_idx -= 1
    else:
        problems[problem_idx].append(int("".join(current_num)))
    
    col_idx -= 1

print(problems)

total = 0

#run math
for index, symbol in enumerate(instructions[-1].split()):
    if symbol == "*":
        value = 1
        for n in problems[index]:
            value *= n
        
    elif symbol == "+":
        value = sum(problems[index])
    
    total += value

print(total)

#4580995422905 part1 answer

#10875057285868 part2 answer