import re

with open("2020/day9.txt") as text_file:
  text = text_file.read()

input = text.split("\n")
for i in range(len(input)):
  input[i] = int(input[i])

def test(number):
  starting_index = input.index(number)
  list = [number]
  search = 167829540
  for number in input[starting_index+1:]:
    #print(list)
    list.append(number)
    added = sum(list)
    if added < search:
      continue
    if added == search:
      print(min(list) + max(list))
      return True
    if added > search:
      return False


for number in input:
  if test(number):
    break


#INVALID NUM = 167829540
