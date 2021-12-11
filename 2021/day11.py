import re
import itertools
import numpy as np
import time

#instructions = open("2021/day11testinput.txt").read().splitlines()
instructions = open("2021/day11input.txt").read().splitlines()

instructions = [[int(i) for i in x] for x in instructions]
grid = np.asarray(instructions)

def find_neighbors(grid, row_index, point_index): #shamelessly stolen from MYSELF HAHA (day11 2020)
  slopes = [(-1, -1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)] #The slopes to check
  nieghbors = []
  for slope in slopes:
    current_pos = [row_index, point_index]
    current_pos[0] += slope[0] #Move by x of slope
    current_pos[1] += slope[1] #Move by y of slope
    if current_pos[0] < 0 or current_pos[0] >= len(grid) or current_pos[1] < 0 or current_pos[1] >= len(grid[row_index]): #if it is out of bounds, skip
      continue
    else:
      nieghbors.append((current_pos[0], current_pos[1]))
  return nieghbors

def step_one(grid): #add one to all energy levels
  for row_index, row in enumerate(grid):
    for point_index, _ in enumerate(row):
      grid[row_index][point_index] += 1

def step_two(grid): #check for fully charged octopi
  charged_list = []
  flashed_once_list = []
  for row_index, row in enumerate(grid):
    for point_index, _ in enumerate(row):
      if grid[row_index][point_index] > 9:
        charged_list.append((row_index, point_index))
        flashed_once_list.append((row_index, point_index))
  while charged_list:
    row_index, point_index = charged_list[0]
    charged_list = charged_list[1:]
    neighbors = find_neighbors(grid, row_index, point_index)
    for n_row_index, n_point_index in neighbors:
      grid[n_row_index][n_point_index] += 1
      if grid[n_row_index][n_point_index] > 9 and (n_row_index, n_point_index) not in flashed_once_list:
        charged_list.append((n_row_index, n_point_index))
        flashed_once_list.append((n_row_index, n_point_index))
  return flashed_once_list

def step_three(grid, flashed_list):
  for row_index, point_index in flashed_list:
    grid[row_index][point_index] = 0

flashed_count = 0
for i in range(300):
  step_one(grid)
  flashed_list = step_two(grid)
  step_three(grid, flashed_list)
  flashed_count += len(flashed_list)

  if len(flashed_list) == len(grid) * len(grid[0]):
    print(i + 1)

print(flashed_count)

#1721 part1 first try! even got to reuse some diagonal neighbor code from a year ago
#step 298 first try! didn't even have to change my code, just a quick new conditional and we all good