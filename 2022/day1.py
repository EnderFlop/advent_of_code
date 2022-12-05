import re
import itertools
import numpy as np
import time

#instructions = open("2022/day1testinput.txt").read()
instructions = open("2022/day1input.txt").read()

elves = instructions.split("\n\n")
food_elves = []
for elf in elves:
  local_total = 0
  foods = elf.split("\n")
  for food in foods:
    local_total += int(food)
  food_elves.append(local_total)

maximum = max(food_elves)
print(maximum, food_elves.index(maximum) + 1)

#part1: 70369 first try!
