import re
import itertools
import numpy as np
import time

instructions = open("2025/day2testinput.txt").read().split(",")
#instructions = open("2025/day2input.txt").read().split(",")

total = 0

for pair in instructions:
  print("i: ", pair)
  first, second = pair.split("-")
  tmp_total = 0

  index = 1
  while index <= len(first) // 2:
    #if len of segment doesn't fit into our number evenly, skip
    if len(first) % index != 0:
      index += 1
      continue

    #get segment we will repeat
    repeat = first[:index]
    num_times_to_repeat = len(first) // index
    repeated = repeat * num_times_to_repeat
    
    while int(first) <= int(repeated) <= int(second):
      tmp_total += int(repeated)

      repeat = str(int(repeat) + 1)

      num_times_to_repeat = max(len(first), len(second)) // len(repeat)
      repeated = repeat * num_times_to_repeat
    
    print(tmp_total)


    index += 1

# 31000881061 correct day 1