import re
import itertools
import numpy as np
import time
import string
import math

instructions = open("2016/day6.txt").read().splitlines()
fake_array = []
for row in instructions:
  fake_array.append(list(row))

array = np.asarray(fake_array)
end_string = ""

for x_index in range(8):
  y_index = 0
  alphabet_dict = {k:0 for k in string.ascii_lowercase}
  #load up alphabet_dict
  while y_index < len(array):
    alphabet_dict[array[y_index][x_index]] += 1
    y_index += 1
  #find most common letter
  largest_value = math.inf
  largest_letter = ""
  letter_dict = {k:v for k,v in alphabet_dict.items() if v != 0}
  for k, v in letter_dict.items():
    if v < largest_value:
      largest_value = v
      largest_letter = k
  end_string += largest_letter

print(end_string)
#part1 wkbvmikb first try! even reused some code from day4
#part2 evakwaga first try! did this challenge super fast, maybe like ten minutes in all. super surprised my dict comprehension worked first try too!