import re
import itertools
import numpy as np
import time

#instructions = open("2025/day4testinput.txt").read().splitlines()
instructions = open("2025/day4input.txt").read().splitlines()

def check_neighbors(grid, r, c):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for y, x in directions:
        new_r = r + y
        new_c = c + x
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            if grid[new_r][new_c]  == "@":
                count += 1
    return count

reachable = 0

for r, row in enumerate(instructions):
    for c, val in enumerate(row):
        if instructions[r][c] == ".":
            continue

        if check_neighbors(instructions, r, c) < 4:
            reachable += 1

print(reachable)

#1393 day1 answer