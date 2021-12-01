import re
import itertools
import numpy as np
import time

instructions = open("2021/day1.txt").read().splitlines()

increase_count = 0
for index in range(len(instructions) - 2):
  if index != 0:
    past_window = sum([int(i) for i in instructions[index-1:index+2]])
    current_window = sum([int(i) for i in instructions[index:index+3]])
    if current_window > past_window:
      increase_count += 1

print(increase_count)
#1297 too low. I just tried to go fast, didn't check my answer lol
#it was 1298. I forgot to change to int :(
#1248 part 2 first try.