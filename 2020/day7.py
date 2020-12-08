import re
import itertools

with open("2020/day7.txt") as text_file:
  text = text_file.read()
text = text.split("\n")

rules_dict = {}

for rule in text:
  split = rule.split(" ")
  bag = " "
  bag = bag.join(split[:2])
  contains = re.findall(r"\d\s\w+\s\w+", rule)
  if split[4] == "no":
    #Add a dictionary or something idk
    rules_dict[bag] = {}
  for container in contains:
    number = container[0]
    container = container[2:]
    rules_dict.setdefault(bag, {})[container] = number

#If container not in rules_dict, add it as an empty dictionary.

def bag_search(string):
  #print(f"searching {string}")
  if "shiny gold" in rules_dict[string]:
    #print(f"\n{string} is shiny gold")
    return True
  elif rules_dict[string] == {}: #If the dictionary is empty, return false
    return False
  for bag in rules_dict[string].keys():
    if bag_search(bag):
      return True

gold_count = 0
for key in rules_dict.keys():
  print(f"\nsearching {key}")
  if bag_search(key):
    gold_count += 1
print(gold_count)