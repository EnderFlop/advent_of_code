import re
import itertools
import numpy as np
import time

#instructions = open("2025/day1testinput.txt").read().splitlines()
instructions = open("2025/day1input.txt").read().splitlines()

total = 0
i = 50

for instruction in instructions:
  direction = instruction[0]
  rotation = int(instruction[1:])
  if direction == "R":
    i += rotation
  elif direction == "L":
    i -= rotation
  i %= 100
  if i == 0:
    total += 1

print(total)