import re
import itertools
import numpy as np
import time

#instructions = open("2025/day1testinput.txt").read().splitlines()
instructions = open("2025/day1input.txt").read().splitlines()

total = 0
i = 50

for instruction in instructions:
  print(instruction)
  print("B", i)

  direction = instruction[0]
  rotation = int(instruction[1:])

  #R1000 points at 0 ten times.
  if rotation // 100:
    print("spin" * (rotation // 100))
    total += rotation // 100 #add any full rotations

  remaining_rotation = rotation % 100

  if direction == "R":
    new_i = i + remaining_rotation
  elif direction == "L":
    new_i = i - remaining_rotation

  if i != 0 and (new_i < 0 or new_i > 100):
    print("trigger")
    total += 1

  i = new_i % 100
  print("F", i)
  if i == 0:
    print("land")
    total += 1 


print(total)

#2577 too low
#6246 too high
#6027 correct