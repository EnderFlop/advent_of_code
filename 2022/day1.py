import re
import itertools
import numpy as np
import time

#instructions = open("2022/day1testinput.txt").read()
instructions = open("2022/day1input.txt").read()

elves = instructions.split("\n\n")
food_elves = []
for elf in elves:
  local_total = 0
  foods = elf.split("\n")
  for food in foods:
    local_total += int(food)
  food_elves.append(local_total)

top_three = 0
for i in range(3):
  maximum = max(food_elves)
  top_three += maximum
  food_elves.remove(maximum)
print(top_three)

#part1: 70369 first try!
#part2: 11546469 too high. didnt even read problem lol
#       203002 second try! easy once i realized what the goal was.