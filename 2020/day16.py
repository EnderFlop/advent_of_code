import re
import itertools
import time
from rich.traceback import install
from rich.console import Console
install()
console = Console()

asdf = open("2020/day16.txt").read().split("\n\n")

rules = asdf[0].split("\n") #List of rule names and the 2 ranges they occupy
my_ticket = asdf[1].split("\n")[1:] #list of a single csv of your ticket
other_tickets = asdf[2].split("\n")[1:] #csv of several tickets in a list
start_time = time.time()

rules_list = []
for rule in rules:
  ranges = re.findall(r"\d+-\d+", rule)
  range_0 = ranges[0].split("-")
  range_1 = ranges[1].split("-")
  rules_list.append((range_0, range_1))

error_rate = 0
for i in other_tickets:
  ticket = i.split(",")
  for value in ticket: #For each value
    value = int(value)
    passed = 0
    for rule in rules_list: #If the value passes at least one of the tests, the value is valid
      range_0 = rule[0]
      range_1 = rule[1]
      if value in range(int(range_0[0]), int(range_0[1]) + 1) or value in range(int(range_1[0]), int(range_1[1]) + 1):
        continue
      else:
        passed += 1
    if passed == len(rules_list):
      error_rate += value

console.log(error_rate)
console.log(f"Took {time.time() - start_time} seconds")

#24033 is too high
#20048 FOR PART 1