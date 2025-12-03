import re
import itertools
import numpy as np
import time

#instructions = open("2025/day3testinput.txt").read().splitlines()
instructions = open("2025/day3input.txt").read().splitlines()

total = 0

for i in instructions:
  indexes = [j for j in range(len(i) - 12, len(i))]
  tracker = 0
  #loop
  while tracker != 12:

    current_val = int(i[indexes[tracker]])
    left_offset = 1
    while indexes[tracker] - left_offset >= 0: #while index in range

      if tracker > 0 and (indexes[tracker] - left_offset) <= indexes[tracker - 1]: #if this index is already directly on top of the one below it, continue
        break

      new_val = int(i[indexes[tracker] - left_offset])

      if new_val >= current_val:
        current_val = new_val
        indexes[tracker] -= left_offset
        left_offset = 0

      left_offset += 1
    
    tracker += 1

  battery_total = int("".join(i[k] for k in indexes))
  total += battery_total

print(total)

#17694 ans part 1

#175659236361660 ans part 2