import re
import itertools
import numpy as np
import time

#instructions = open("2021/day14testinput.txt").read().splitlines()
instructions = open("2021/day14input.txt").read().splitlines()

polymer = instructions[0]
insertions = {}
for i in instructions[2:]:
  a, b = i.split(" -> ")
  insertions[a] = b

for i in range(10):
  new_polymer = ""
  for current_index in range(len(polymer) - 1):
    elem_one = polymer[current_index]
    elem_two = polymer[current_index + 1]
    chain = elem_one + elem_two
    if chain in insertions.keys():
      new_polymer += elem_one + insertions[chain]
  new_polymer += elem_two
  polymer = new_polymer

count = {}
for letter in polymer:
  if letter in count.keys():
    count[letter] += 1
  else:
    count[letter] = 1

max_elem = 0
min_elem = 999999999999999999999999999999999999

for elem, num in count.items():
  if num > max_elem:
    max_elem = num
  if num < min_elem:
    min_elem = num

print(max_elem - min_elem)
#2891 part1 first try. Next part says to run the loop 40 times which i'm fairly sure is roughly 2^40. i doubt my pc can take that with this implimentation.