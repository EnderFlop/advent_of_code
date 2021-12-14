import re
import itertools
import numpy as np
import time
import collections

#instructions = open("2021/day14testinput.txt").read().splitlines()
instructions = open("2021/day14input.txt").read().splitlines()


def string_to_polymer(string):
  polymer = collections.defaultdict(lambda: 0)
  for index in range(len(string) - 1):
    polymer[string[index] + string[index + 1]] += 1
  return polymer

polymer = string_to_polymer(instructions[0])

insertions = {}
for i in instructions[2:]:
  a, b = i.split(" -> ")
  insertions[a] = b


#now it is an optimization problem. how can i perserve the pairs without keeping copies of them?
#have a dict of all pairs. {HK: 1}. iterate through and add pairs {HK:1, HB:1, BK:1}, {HK:1, HB:2, BK:2, HO:1, OB:1, BP:1, PK;1}
for i in range(40):
  new_dict = collections.defaultdict(lambda: 0)
  for chain, count in polymer.items():
    chain_one = chain[0] + insertions[chain]
    chain_two = insertions[chain] + chain[1]
    new_dict[chain_one] += count
    new_dict[chain_two] += count
  print(new_dict)
  polymer = new_dict.copy()

#STEP_3 = "NBBBCNCCNBBNBNBBCHBHHBCHB"
#STEP_4 = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
#print(string_to_polymer(STEP_4))
#the dictionary function works perfectly, it must be the counting function that is having a problem.

elem_count = collections.defaultdict(lambda: 0)
for chain, count in polymer.items():
  elem_count[chain[0]] += count
elem_count[chain[1]] += 1 #adding final elem


max_elem = 0
min_elem = 9999999999999999999999999999999999999999999999

print(elem_count)
for elem, num in elem_count.items():
  if num > max_elem:
    max_elem = num
  if num < min_elem:
    min_elem = num

print(max_elem - min_elem)
#2891 part1 first try. Next part says to run the loop 40 times which i'm fairly sure is roughly 2^40. i doubt my pc can take that with this implimentation.
#4607749009683 part2. I'm gonna be real I don't know why the elem_count[chain[1]] += 1 is the solution to the problem. I figure you would have to add "count", not 1.
# butttt, it isn't right when you do that, so whatever. glad my optimization theory worked first try!