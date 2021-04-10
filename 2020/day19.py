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

def construct_rule(rule_number):
  related_rules = rules_dict[rule_number]
  matches = []
  print(rule_number, related_rules)
  if related_rules[0] in ["\"b\"", "\"a\""]: #If the rule is just a character
    return related_rules[0][1:-1] #Return that character
  elif "|" in related_rules:
    possibility_one = related_rules[0:2]
    possibility_two = related_rules[3:]
  else:
    end_string = ""
    for related in related_rules:
      end_string += construct_rule(related)
    return end_string
  return matches


possible_matches = construct_rule("0")
print(possible_matches)