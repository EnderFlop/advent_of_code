import re
import itertools
import numpy as np
import time
from queue import Queue

#instructions = open("2021/day9testinput.txt").read().splitlines()
instructions = open("2021/day9input.txt").read().splitlines()

grid = []
for row in instructions:
  grid_row = []
  for num in row:
    grid_row.append(num)
  grid.append(grid_row)

grid = np.asarray(grid)


low_points = []
for row_index, row in enumerate(grid):
  for point_index, point in enumerate(row):
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
      low_points.append((row_index, point_index))


#must preform some kind of breath first search. 
# how about starting at a given point, the lowest point, and expanding out from there in all directions, changing the value of the things it hits.
# every point which is hit is added to the queue. it scans all of it's four cardinal paths and if it finds a point that hasn't been hit, it adds it to the queue
basin_sizes = []
for row_index, point_index in low_points:
  temp_basin_size = 0
  queue = Queue()
  queue.put((row_index, point_index))
  while not queue.empty():
    row_index, point_index = queue.get()
    row = grid[row_index]
    point = row[point_index]

    if point != "u": 
      grid[row_index][point_index] = "u"
      temp_basin_size += 1
    
    left = list(row[:point_index])
    right = list(row[point_index + 1:])
    up = list(grid[:row_index,point_index])
    down = list(grid[row_index + 1:, point_index])
    #we have to iterate through all of them (up and left backwards because) and if we hit a wall (9), stop. otherwise append to queue.
    left.reverse()
    up.reverse()
    
    #if the point has been seen, it is only useful if it is NOT surrounded by u's and walls. it needs to have found a new path to explore.
    check_left = any(elem in ["0","1","2","3","4","5","6","7","8"] for elem in left) #If left contains a number
    check_right = any(elem in ["0","1","2","3","4","5","6","7","8"] for elem in right)
    check_up = any(elem in ["0","1","2","3","4","5","6","7","8"] for elem in up)
    check_down = any(elem in ["0","1","2","3","4","5","6","7","8"] for elem in down)

    if check_left:
      for index, x in enumerate(left):
        if x == "9" or x == "u":
          break
        grid[row_index][point_index - (index + 1)] = "u"
        queue.put((row_index, point_index - (index + 1)))
        temp_basin_size += 1
    if check_up:
      for index, x in enumerate(up):
        if x == "9" or x == "u":
          break
        grid[row_index - (index + 1)][point_index] = "u"
        queue.put((row_index - (index + 1), point_index))
        temp_basin_size += 1
    if check_right:
      for index, x in enumerate(right):
        if x == "9" or x == "u":
          break
        grid[row_index][point_index + (index + 1)] = "u"
        queue.put((row_index, point_index + (index + 1)))
        temp_basin_size += 1
    if check_down:
      for index, x in enumerate(down):
        if x == "9" or x == "u":
          break
        grid[row_index + (index + 1)][point_index] = "u"
        queue.put((row_index + (index + 1), point_index))
        temp_basin_size += 1
      #all the points visible from the chosen point are marked.
  basin_sizes.append(temp_basin_size)

print(basin_sizes)
basin_sizes.sort()
result = 1
for x in basin_sizes[-3:]:
  result *= x
print(result)


#489 part1
#1056330 part2! first try too! this one was crazy. I had to implement my own weird breath first search algorithm on a np graph.
#i had to deal with numbers seeing other numbers through walls and all sorts of stuff
#its funny, I wrote that we should start at the low points, and part 1 clearly leads you in that direction,
# but I still tried a weird algorithm where you iterate over every point before I settled on this.
#it took another two hours, just like last problem. I hope they throw an easy one at me soon.
#p.s. don't judge me for my part1/low_points code. I was doing it fast :)