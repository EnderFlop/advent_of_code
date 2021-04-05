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

#LOGIC TO SORT FOR VALID TICKETS
#valid_tickets = [[1,2,3,4,5], [2,3,4,5,6]] /List of lists that are valid tickets
valid_tickets = []
for ticket in other_tickets:
  seperated_ticket = ticket.split(",")
  ticket_passed = True
  for value in seperated_ticket:
    value = int(value)
    rules_failed = 0
    for rule_ranges in rules_dict.values():
      range_1, range_2 = rule_ranges[0], rule_ranges[1]
      if value not in range(range_1[0], range_1[1] + 1) and value not in range(range_2[0], range_2[1] + 1):
        rules_failed += 1
    if rules_failed == len(rules_dict):
      ticket_passed = False
  if ticket_passed:
    valid_tickets.append(seperated_ticket)

#All of the numbers in a given field on every ticket will follow one rule. 
rule_to_field = {key: [] for key in rules_dict.keys()}
#Get the numbers from a field from every ticket
#For each value, see if the rule works. If a value fails, try the next rule. If it all passes, set rule_to_field[rule] = field_number
#Continue until len(rule_to_field) == len(rules)

for index in range(len(rules)): #for each field
  values_at_index = [int(ticket[index]) for ticket in valid_tickets] #get all the values there
  valid_rules_at_index = 0
  for rule, rule_ranges in rules_dict.items(): #for each rule
    range_1, range_2 = rule_ranges[0], rule_ranges[1]
    rule_passed = True
    for value in values_at_index: #for each value
      if value not in range(range_1[0], range_1[1] + 1) and value not in range(range_2[0], range_2[1] + 1): #if the value does not pass the rule, this rule has failed
        #print(f"{value} not in ranges {range_1}, {range_2}, so rule {rule} failed for field {index}.")
        rule_passed = False
    if rule_passed: #If the rule passes, then one more rule works at this index
      rule_to_field[rule].append(index)

print(rule_to_field)

#rule_to_field is now a dict of rules and the indexes they are valid at. Some rules only have 1 valid index. 
#Set this rule to that index, then remove that index from all other rules. Run again.

real_final_dict = {}
while len(real_final_dict) != len(rules):
  for rule, indexes in rule_to_field.items():
    if len(indexes) == 1:
      real_final_dict[rule] = indexes[0]
      break
  del rule_to_field[rule]
  for rule, other_indexes in rule_to_field.items():
    if indexes[0] in other_indexes:
      rule_to_field[rule].remove(indexes[0])
print(real_final_dict)

#real_final_dict is now a dict of "rule":index pairs. Iterate through them, if the rule starts with "departure"
#get the value of that index in my ticket and multiply them all together
part2 = 1
my_ticket = my_ticket[0].split(",")
for key, value in real_final_dict.items():
  if key.split(" ")[0] == "departure":
    part2 *= int(my_ticket[value])

print(part2)
#PART 2 = 4810284647569 FIRST TRY

