import re
import itertools
import numpy as np
import time

#instructions = open("2025/day3testinput.txt").read().splitlines()
instructions = open("2025/day3input.txt").read().splitlines()

total = 0
for i in instructions:
  left = 0
  best = 0

  while left != len(i) - 1:
    l = i[left]
    r = max(i[left + 1:])
    res = int(str(l) + str(r))
    best = max(res, best)
    left += 1

  total += best

print(total)
#17694 ans part 1