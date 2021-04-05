import re
import itertools

asdf = open("2020/day16.txt").read().split("\n\n")

rules = asdf[0].split("\n") #List of rule names and the 2 ranges they occupy
my_ticket = asdf[1].split("\n")[1:] #list of a single csv of your ticket
other_tickets = asdf[2].split("\n")[1:] #csv of several tickets in a list

#rules_dict; "Rule": ([start1, end1], [start2, end2])
rules_dict = {}
for rule in rules:
  title = rule.split(":")[0]
  ranges = re.findall(r"\d+-\d+", rule)
  range1 = [int(i) for i in ranges[0].split("-")]
  range2 = [int(i) for i in ranges[1].split("-")]
  rules_dict[title] = (range1, range2)


scanning_error_rate = 0
for ticket in other_tickets:
  seperated_ticket = ticket.split(",")
  for value in seperated_ticket:
    value = int(value)
    rules_failed = 0
    for rule_ranges in rules_dict.values():
      range_1, range_2 = rule_ranges[0], rule_ranges[1]
      if value not in range(range_1[0], range_1[1] + 1) and value not in range(range_2[0], range_2[1] + 1):
        rules_failed += 1
    if rules_failed == len(rules_dict):
      scanning_error_rate += value
        

print(scanning_error_rate)