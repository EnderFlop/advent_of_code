import re
import itertools
import numpy as np

starting = open("2020/day17.txt").read()
#print(starting)

#    .#.
#    ..#
#    ###

a = np.loadtxt("2020/day17.txt", dtype=str, comments="x") 
starting_array = np.full((8,8), "a", dtype=str)
for line_index in range(a.size):
  new_line = np.array(list(a[line_index]), dtype=str)
  starting_array[line_index] = new_line

print(starting_array)

#Some function that checks all nearby neighbors
