import re
import itertools
import numpy as np
import time

#instructions = open("2021/day8testinput.txt").read().splitlines()
instructions = open("2021/day8input.txt").read().splitlines()

output_count = 0
for i in instructions:
  signal_patterns = i.split("|")[0].split()
  output_values = i.split("|")[1].split()
  print(output_values)
  for o in output_values:
    length = len(o)
    if length == 2 or length == 7 or length == 3 or length == 4:
      output_count += 1
  print(output_count)

print(output_count)
#416 part1