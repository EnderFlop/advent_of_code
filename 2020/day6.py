import re
import string

with open("2020/day6.txt") as text_file:
  text = text_file.read()

groups = text.split("\n\n")

total_answers = 0
for group in groups:
  person_list = group.split("\n")
  answer_list = {}
  for person in person_list:
    for char in person:
      if char not in answer_list:
        answer_list[char] = 1
      else:
        answer_list[char] += 1
  for value in answer_list.values(): 
    if value == len(person_list):
      total_answers += 1

print(total_answers)