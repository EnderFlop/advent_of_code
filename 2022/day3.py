import re
import itertools
import numpy as np
import time
import string

#instructions = open("2022/day3testinput.txt").read().splitlines()
instructions = open("2022/day3input.txt").read().splitlines()

letter_lookup = string.ascii_letters
priorities = 0
for rucksack in instructions:
  ruck_len = len(rucksack)
  one, two = rucksack[:ruck_len//2], rucksack[ruck_len//2:]
  shared_items = list(set([char for char in one if char in two]))
  priorities += letter_lookup.index(shared_items[0]) + 1

print(priorities)
#part1 7746 first try!