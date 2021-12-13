import re
import itertools
import numpy as np
import time

#instructions = open("2021/day13testinput.txt").read().splitlines()
instructions = open("2021/day13input.txt").read().splitlines()

coords = []
folds = []
max_x = 0
max_y = 0
instruction_pointer = False
for i in instructions:
  if i == "":
    instruction_pointer = True
    continue
  if instruction_pointer:
    folds.append(i)
  else:
    x, y = i.split(",")
    x, y = int(x), int(y)
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y
    coords.append((x, y))


#grid max_x long and max_y high.
grid = [["." for x in range(max_x + 1)] for y in range(max_y + 1)]
grid = np.asarray(grid)

for x, y in coords:
  grid[y][x] = "#"

for fold in folds:
  a, index = fold.split("=")
  axis = a[-1]
  index = int(index)

  if axis == "y":
    grid_one, grid_two = np.split(grid, axis=0, indices_or_sections=[index])
    grid_two = np.flipud(grid_two)
    grid_two = grid_two[:-1]

  if axis == "x":
    grid_one, grid_two = np.split(grid, axis=1, indices_or_sections=[index])
    grid_two = np.fliplr(grid_two)
    grid_two = grid_two[:,[x for x in range(grid_two.shape[1] - 1)]]
  
  for row_index, row in enumerate(grid_two):
    for point_index, point in enumerate(row):
      if point == "#":
        x_offset = len(grid_one) - len(grid_two)
        y_offset = len(grid_one[0]) - len(grid_two[0])
        grid_one[row_index + x_offset][point_index + y_offset] = "#"
  grid = grid_one

for row_index, row in enumerate(grid):
  row_str = ""
  for point_index, point in enumerate(row):
    if point == ".":
      row_str += " "
    elif point == "#":
      row_str += "#"
  print(row_str)
  
#759 part 1 first try!
#HOGAZKPR not right, i just tried to guess the blurry letters. something is going wrong
#HECRZKPR second try! I just implimented a quick fix i found online. 
#my suspicion that I was folding incorrectly was sort of right, turns out it was more ugly index math I wasn't accounting for.
#it's rough when it works on the test input but the real input is completely unbugfixable.