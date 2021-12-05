import re
import itertools
import numpy as np
import time

#instructions = open("2021/day5testinput.txt").read().splitlines()
instructions = open("2021/day5input.txt").read().splitlines()

biggest_x, biggest_y = 0, 0
coord_sets = []
for i in instructions:
  i = i.split(" -> ")
  x1, y1, x2, y2 = i[0].split(",")[0], i[0].split(",")[1], i[1].split(",")[0], i[1].split(",")[1]
  x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
  coord_sets.append(((x1, y1), (x2, y2)))
  if max(x1, x2) > biggest_x:
    biggest_x = max(x1, x2)
  if max(y1, y2) > biggest_y:
    biggest_y = max(y1, y2)

grid = np.zeros((biggest_x + 1, biggest_y + 1), dtype=int)
#the grid system works in the fourth quadrant, so (0,0) is the top left and (9,9) is the bottom right.

for coords in coord_sets:
  x1, y1, x2, y2 = coords[0][0], coords[0][1], coords[1][0], coords[1][1]
  #part1: only consider straight lines
  if x1 == x2:
    lower_y = min(y1, y2)
    higher_y = max(y1, y2)
    difference = abs(y1 - y2)
    for i in range(0, difference + 1):
      grid[lower_y + i][x1] += 1
  if y1 == y2:
    lower_x = min(x1, x2)
    higher_x = max(x1, x2)
    difference = abs(x1 - x2)
    for i in range(0, difference + 1):
      grid[y1][lower_x + i] += 1

collision_count = 0
for row in grid:
  for unit in row:
    if unit >= 2:
      collision_count += 1

print(collision_count)
#4993 first try!