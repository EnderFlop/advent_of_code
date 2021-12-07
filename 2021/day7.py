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
    distance = abs(crab - i)
    fuel_use += ((distance**2 + distance)/2)
  if min_fuel_use > fuel_use:
    min_fuel_use = fuel_use

print(min_fuel_use)
#342534 part1 first try!
#94004208 part2 first try! RANK 903 on the leaderboard!!!!
#googled "factorial but addition" and plugged in the first formula that looked decent ((n^2 + n)/2) and it worked!