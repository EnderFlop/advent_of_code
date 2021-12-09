import re
import itertools
import numpy as np
import time

#instructions = open("2021/day9testinput.txt").read().splitlines()
instructions = open("2021/day9input.txt").read().splitlines()

grid = [[x[i] for i in range(len(x))] for x in instructions]
grid = np.asarray(grid)

low_points = 0
for row_index in range(len(grid)):
  for point_index in range(len(grid[row_index])):
    surrounding_points = []
    point = grid[row_index][point_index]

    try:
      surrounding_points += grid[row_index + 1][point_index]
    except IndexError:
      pass
    try:
      surrounding_points += grid[row_index - 1][point_index]
    except IndexError:
      pass
    try:
      surrounding_points += grid[row_index][point_index + 1]
    except IndexError:
      pass
    try:
      surrounding_points += grid[row_index][point_index - 1]
    except IndexError:
      pass

    if point < min(surrounding_points):
      low_points += int(point) + 1

print(low_points)