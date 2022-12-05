import re
import itertools
import numpy as np
import time

#instructions = open("2022/day4testinput.txt").read().splitlines()
instructions = open("2022/day4input.txt").read().splitlines()

full_overlaps = 0
for pair in instructions:
  elf1, elf2 = pair.split(",")
  ass1, ass2 = int(elf1.split("-")[0]), int(elf1.split("-")[1])
  ass3, ass4 = int(elf2.split("-")[0]), int(elf2.split("-")[1])
  if ass3 in range(ass1, ass2 + 1) or ass4 in range(ass1, ass2 + 1) or ass1 in range(ass3, ass4 + 1) or ass2 in range(ass3, ass4 + 1):
    #print(f"{ass1}-{ass2}|{ass3}-{ass4}")
    full_overlaps += 1

print(full_overlaps)
#part1 490 first try!
#part2 921 first try!