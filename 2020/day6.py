import re

with open("2020/day6.txt") as text_file:
  text = text_file.read()

groups = text.split("\n\n")

total_answers = 0
for group in groups:
  person_list = group.split("\n")
  answer_list = []
  for person in person_list:
    for char in person:
      if char not in answer_list:
        answer_list.append(char)
  total_answers += len(answer_list)

print(total_answers)