import re
import itertools
import numpy as np
import time

#instructions = open("2025/day4testinput.txt").read().splitlines()
instructions = open("2025/day4input.txt").read().splitlines()

def modify_grid(grid, pairs):
    for y, x in pairs:
        grid[y] = grid[y][:x] + "." + grid[y][x + 1:]

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
new_reachable = 0
while True:

    valid_rolls = []
    for r, row in enumerate(instructions):
        for c, val in enumerate(row):
            if instructions[r][c] == ".":
                continue

            if check_neighbors(instructions, r, c) < 4:
                new_reachable += 1
                valid_rolls.append((r, c))
    
    if new_reachable == reachable: #if total did not change (no new paper was removed)
        break

    else:
        modify_grid(instructions, valid_rolls)
        reachable = new_reachable

print(reachable)

#1393 part1 answer
#8643 part2 answer