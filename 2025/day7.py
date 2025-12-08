import re
import itertools
import numpy as np
import time

#instructions = open("2025/day7testinput.txt").read().splitlines()
instructions = open("2025/day7input.txt").read().splitlines()

#get beam indexes (all | or S in row)
#cast beam beneath (read row below)
#   if index below is a ., turn to a |
#   if index below is a ^, turn left and right into |

def insert_char(string, insert, index):
    return string[:index] + insert + string[index + 1:]

total = 0

for row_idx in range(len(instructions[:-1])):
    row = instructions[row_idx]
    indexes = [idx for idx, elem in enumerate(row) if elem == "|" or elem == "S"]
    next_row = instructions[row_idx + 1]
    for beam in indexes:
        #if empty, turn to beam
        if next_row[beam] == ".":
            next_row = insert_char(next_row, "|", beam)
        #if splitter, split
        if next_row[beam] == "^":
            total += 1
            if beam - 1 >= 0:
                next_row = insert_char(next_row, "|", beam - 1) 
            if beam + 1 < len(next_row):
                next_row = insert_char(next_row, "|", beam + 1)
        instructions[row_idx + 1] = next_row

#print(instructions)
#print(instructions[-1].count("|"))
print(total)

#1546 part1 answer