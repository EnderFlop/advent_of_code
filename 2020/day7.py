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
    rules_dict[bag] = {}
  for container in contains:
    number = int(container[0])
    container = container[2:]
    rules_dict.setdefault(bag, {})[container] = number

def count_bags_inside(string):
  bags = rules_dict[string] #Dict of all bags in current bag
  count = 0 #init count
  if bags == {}: #If empty, return 0 because no bags are in it
      print(f"{string} empty, returning 0")
      return 0
  print(f"bags = {bags}")
  for bag in bags: #For each bag
    print(f"adding {rules_dict[string][bag]}")
    count += bags[bag] #Add amount of current bag
    print(f"going into {bag}")
    count += bags[bag] * count_bags_inside(bag) #Add amount of current bag (the coefficient) * the amount of bags inside the bag to the count
  return count #return a count of all the bags inside the current bag

print("\n\n\n\n\n")
print(count_bags_inside("shiny gold"))

#not 4444444444, too high
#not 8140, too low
#18925!!