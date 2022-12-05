import re
import itertools
import numpy as np
import time
import string

#instructions = open("2022/day3testinput.txt").read().splitlines()
instructions = open("2022/day3input.txt").read().splitlines()

letter_lookup = string.ascii_letters
i = 0
priorities = 0
while i < len(instructions):
  one, two, three = instructions[i], instructions[i + 1], instructions[i + 2]
  shared_items = list(set([char for char in one if char in two and char in three]))
  print(shared_items)
  priorities += letter_lookup.index(shared_items[0]) + 1
  i += 3

print(priorities)
#part1 7746 first try!
#part2 2604 first try!