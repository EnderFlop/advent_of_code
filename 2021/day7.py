import re
import itertools
import numpy as np
import time
import math

#instructions = open("2021/day7testinput.txt").read().split(",")
instructions = open("2021/day7input.txt").read().split(",")

crabs = [int(i) for i in instructions]
min_position = min(crabs)
max_position = max(crabs)

min_fuel_use = math.inf
for i in range(min_position, max_position + 1):
  fuel_use = 0
  for crab in crabs:
    fuel_use += abs(crab - i)
  if min_fuel_use > fuel_use:
    min_fuel_use = fuel_use

print(min_fuel_use)
#342534 part1 first try!