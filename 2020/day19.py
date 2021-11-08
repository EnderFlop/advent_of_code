import re
import itertools
import numpy as np
import time

text = open("2020/day19.txt").read()
rules, messages = text.split("\n\n")
rules = rules.splitlines()
messages = messages.splitlines()
rules_dict = {}
for rule in rules:
  split = rule.split(": ")
  rules_dict[split[0]] = str(split[1:])[2:-2].split(" ")

#rules_dict is formatted; 'num': ['rule1', 'rule2']

#Given a rule number
#If the rule is a letter, then the rule is a letter. return it
#If the rule is only subrules, then the rule = the result of those sub rules as a list
#If the rule is two possible sub-rules matches, then the result is a list of the results of those two sub-rules

def distribute_list(list1, list2):
  combined_list = []
  for string1 in list1:
    for string2 in list2:
      combined_list.append(string1 + string2)
  return combined_list

def construct_rule(rule_number):
  related_rules = rules_dict[rule_number]
  print(rule_number, related_rules)
  if related_rules[0] in ["\"b\"", "\"a\""]: #If the rule is just a character
    return [related_rules[0][1:-1]] #Return that character
  elif "|" in related_rules:
    possibility_one = related_rules[0:2] #First set of subrules
    possibility_two = related_rules[3:] #Second set of subrules
    first_set = []
    second_set = []
    for rule in possibility_one:
      first_set += (construct_rule(rule))
    first_set = "".join(first_set)
    for rule in possibility_two:
      second_set += (construct_rule(rule))
    second_set = "".join(second_set)
    print(first_set, second_set)
    return [first_set, second_set]
  else:
    returned_strings = []
    for related in related_rules: #Construct the rules
      returned_strings.append(construct_rule(related)) 
    print(returned_strings)
    if len(returned_strings) == 2:
      return distribute_list(returned_strings[0], returned_strings[1])
    if len(returned_strings) == 1:
      return returned_strings


possible_matches = construct_rule("0")
print(possible_matches)

