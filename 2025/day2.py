import re
import itertools
import numpy as np
import time

#instructions = open("2025/day2testinput.txt").read().split(",")
instructions = open("2025/day2input.txt").read().split(",")

total = 0

for pair in instructions:
  print("i: ", pair)
  first, second = pair.split("-")
  found = set()
  tmp_total = 0

  print(pair)
  for i in range(1, int(second[:len(second)//2 + 1])):
    if len(first) % len(str(i)) == 0:
      times_to_repeat = len(first) // len(str(i))
      repeated = str(i) * times_to_repeat
      if times_to_repeat > 1 and int(first) <= int(repeated) <= int(second) and repeated not in found:
        tmp_total += int(repeated)
        print(repeated)

        found.add(repeated)

    #patch, just do again
    if len(first) != len(second) and len(second) % len(str(i)) == 0:
      times_to_repeat = len(second) // len(str(i))
      repeated = str(i) * times_to_repeat
      if times_to_repeat > 1 and int(first) <= int(repeated) <= int(second) and repeated not in found:
        tmp_total += int(repeated)
        found.add(repeated)
    
  total += tmp_total
    
print(total)

# 31000881061 correct day 1

# 46769308485 correct day 2
# brute force ftw