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

rules_list = {} #create a rules dict where KEY = rule title and VALUE = a tuple of lists containing 2 numbers, the start and stops (-1) of their ranges
for rule in rules:
  ranges = re.findall(r"\d+-\d+", rule)
  title = rule.split(":")[0]
  range_0 = ranges[0].split("-")
  range_1 = ranges[1].split("-")
  rules_list[title] = (range_0, range_1)

# THIS IS USED TO DETERMINE WHICH TICKETS ARE VALID. TAKES <0.1 SECONDS
valid_tickets = []
for i in other_tickets:
  ticket = i.split(",")
  ticket_passed = 0
  for value in ticket: #For each value
    value = int(value)
    passed = 0
    for rule in rules_list.values(): #If the value passes at least one of the tests, the value is valid
      range_0 = rule[0]
      range_1 = rule[1]
      if value in range(int(range_0[0]), int(range_0[1]) + 1) or value in range(int(range_1[0]), int(range_1[1]) + 1):
        passed = 1
      else:
        continue
    if passed == 1: #If the value passed at least 1 test, add 1 correct value to the ticket test
      ticket_passed += 1
  if ticket_passed == len(ticket):
    valid_tickets.append(ticket)

#valid_tickets is now a list of all the tickets which pass all the tests.

rule_not_dict = {i: () for i in rules_list.keys()}
#FOR EACH VALID TICKET
  #For each value in ticket
    #For each rule in rules
      #If value passes that rule, mark that rule as a maybe for index [rule]
      #If it doesnt mark that rule as NOT being in that index
for i in other_tickets:
  ticket = i.split(",")
  for value_index in range(len(ticket)): #For each value
    value = int(ticket[value_index])
    for title, rule in rules_list.items(): #If the value doesn't pass the test, this index 
      range_0 = rule[0]
      range_1 = rule[1]
      if value in range(int(range_0[0]), int(range_0[1]) + 1) or value in range(int(range_1[0]), int(range_1[1]) + 1):
        continue
      else:
        list_holder = list(rule_not_dict[title])
        list_holder.append(value_index)
        rule_not_dict[title] = set(list_holder)

#Something is wrong with how indexes chosen to be wrong. The first two items, departure location
#and departure station are both ONLY valid at index 19. This is of course incorrect. Either fix
#the logic behind this or create new logic. 
# 
#Maybe a dict where each key starts with a list of all possible indexes
#and if it can't be that index then that index is removed from the list?

valid_rule_indexes = [i for i in range(len(rule_not_dict))]
print(rule_not_dict)
rule_to_index = {}
#while valid_rule_indexes: #While there exists an index that doesnt have a rule assigned to it yet
for i in range(100):
  for k, v in rule_not_dict.items():
    #print(valid_rule_indexes)
    #print(set(v))
    #Valid_rule_indexes is a list of indexes that do not currently have rules
    #v is a list of indexes that this current rule (k) can NOT exist in
    difference = list(set(valid_rule_indexes) -  set(v))
    #print(difference)
    #difference = all valid values - incorrect values
    if len(difference) == 1: #If there was only one valid index
      valid_index = difference[0] #The only index left must be the valid index
      rule_to_index[k] = valid_index #Set the key equal to that index
      valid_rule_indexes.remove(valid_index) #Remove it from the list of remaining indexes
      for k, v in rule_not_dict.items():
        rule_not_dict[k] = set([x for x in v if x != valid_index])

print(rule_not_dict)
print(rule_to_index)

    


console.log(f"Took {time.time() - start_time} seconds")

#24033 is too high
#20048 FOR PART 1