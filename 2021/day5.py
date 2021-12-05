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
  elif y1 == y2:
    lower_x = min(x1, x2)
    higher_x = max(x1, x2)
    difference = abs(x1 - x2)
    for i in range(0, difference + 1):
      grid[y1][lower_x + i] += 1
  #now for the work on diagonal lines
  elif x1 != x2 and y1 != y2:
    points = []
    #the abs(x1 - x2) and abs(y1 - y2) are always the same, so it will always be a straight diagonal.
    #take (8,0) to (0,8). walking from x=8 to x=0 means the range must be from 8 to zero
    if x1 > x2 and y1 > y2:
      #walk bottom right to top left
      points = list(zip(range(y1, y2 - 1, -1), range(x1, x2 - 1, -1)))
    elif x1 > x2 and y1 < y2:
      #walk top right to bottom left
      points = list(zip(range(y1, y2 + 1), range(x1, x2 -1, -1)))
    elif x1 < x2 and y1 > y2:
      #walk bottom left to top right
      points = list(zip(range(y1, y2 - 1, -1), range(x1, x2 + 1)))
    elif x1 < x2 and y1 < y2:
      #walk top left to bottom right
      points = list(zip(range(y1, y2 + 1), range(x1, x2 + 1)))
    for p in points:
      y, x = p
      grid[y][x] += 1
      


collision_count = 0
for row in grid:
  for unit in row:
    if unit >= 2:
      collision_count += 1

print(collision_count)
#4993 first try!
#21101 first try! thank god, this would have kicked my ass to bug fix. 
# i hate index math :) especially when I design it so the x and y are backwards :) and big y means down :))))