import re
import itertools
import numpy as np
import time

starting = open("2020/day17.txt").read()
#print(starting)

#    .#.
#    ..#
#    ###

start_time = time.time()

a = np.loadtxt("2020/day17.txt", dtype=str, comments="x")
starting_array = np.full((1,8,8), ".", dtype=str) #3x3 grid with 1 depth
for line_index in range(a.size):
  new_line = np.array(list(a[line_index]), dtype=str)
  starting_array[0,line_index,:] = new_line

print(starting_array)

def check_neighbors(array, z, y, x):
  base = array[z,y,x]
  #Check the 26 neighbors around z,y,x.
  neighbors = array[max(0,z-1):z+2, max(0,y-1):y+2, max(0,x-1):x+2].copy() #max, because a neg index returns weird shit
  alive_count = np.count_nonzero(neighbors == "#")
  if base == "#":
    alive_count -= 1
  return alive_count

def step(array):
  z,y,x = array.shape
  new_array = np.full((z+2,y+2,x+2), ".", dtype=str)
  new_array[1:z+1, 1:y+1, 1:x+1] = array.copy() #Pastes the old array into the middle of the new one
  final_array = new_array.copy()
  for z in range(0, new_array.shape[0]):
    for y in range(0, new_array.shape[1]):
      for x in range(0, new_array.shape[2]):
        alive_neighbors = check_neighbors(new_array, z, y, x)
        cell = new_array[z,y,x]
        if cell == "#": #If the cell is alive
          if alive_neighbors == 2 or alive_neighbors == 3: #and more/less than 2 or 3 of its neighbors are also live
            pass
          else:
            final_array[z,y,x] = "."
        elif cell == ".":
          if alive_neighbors == 3:
            final_array[z,y,x] = "#"
  print(final_array)
  return final_array.copy()

for iteration in range(6):
  starting_array = step(starting_array)

print(np.count_nonzero(starting_array == "#"))

end_time = time.time()
print(f"Took {end_time-start_time} seconds")

#PART1 386 FIRST TRY
