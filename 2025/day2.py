import re
import itertools
import numpy as np
import time

#instructions = open("2025/day2testinput.txt").read().split(",")
instructions = open("2025/day2input.txt").read().split(",")

total = 0

for i in instructions:
  first, second = i.split("-")
  tmp_total = 0

  print(first, second)

  #shift to correct place value counts
  if len(first) % 2 == 1 and len(second) % 2 == 1:
    continue
  elif len(first) % 2 == 1:
    first = "1" + "0" * len(first)
  elif len(second) % 2 == 1:
    second = "9" * (len(second) - 1)

  #shift up or down to correct second half inequalities
  first_half_first = first[:len(first) // 2]
  second_half_first = first[len(first) // 2:]
  if int(second_half_first) > int(first_half_first):
    first = str(int(first_half_first) + 1) + "0" * len(second_half_first)

  first_half_second = second[:len(second) // 2]
  second_half_second = second[len(second) // 2:]
  if int(second_half_second) < int(first_half_second):
    second = str(int(first_half_second) - 1) + "9" * len(second_half_second)
  
  print(first, second)

  if len(first) == len(second):
    first_half_first = first[:len(first) // 2]
    first_half_second = second[:len(second) // 2]

    second_half_first = first[len(first) // 2:]
    second_half_second = second[len(second) // 2:]

    for i in range(int(first_half_first), int(first_half_second) + 1):
      if int(first_half_first) >= int(second_half_first) and int(first_half_first) <= int(second_half_second):
        print("f", int(str(i) * 2))
        tmp_total += int(str(i) * 2)

  else:
    print("LEN MISMATCH")
  total += tmp_total

print(total)

# 31000881061 correct day 1