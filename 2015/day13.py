import itertools
import re

with open("2015/day13.txt") as text_file:
  text = text_file.read().splitlines()

happiness_dict = {}
#Happiness_dict formatted like {Bobby:{Alice:2, Carol:4, David:12}, }
for line in text:
  line = line.split()

  name = line[0]
  gain_or_lose = line[2]
  happiness = int(line[3])
  if gain_or_lose == "lose":
    happiness *= -1
  partner = line[-1][:-1]

  if name in happiness_dict:
    happiness_dict[name][partner] = happiness
  else:
    happiness_dict[name] = {partner: happiness}

print(happiness_dict)
happiness_dict["You"] = {}
for k in happiness_dict.keys():
  happiness_dict[k]["You"] = 0
  happiness_dict["You"][k] = 0

possible_seats = itertools.permutations(happiness_dict.keys())
max_happiness = float("-inf")

for table in possible_seats:
  current_happiness = 0
  for seat_index in range(len(table)):
    person = table[seat_index]
    left_person = table[seat_index-1]
    right_person = table[(seat_index+1)%len(table)]
    current_happiness += happiness_dict[person][left_person]
    current_happiness += happiness_dict[person][right_person]
  if current_happiness > max_happiness:
    max_happiness = current_happiness

print(max_happiness)    

#Not 58 cause i fucked up the permutations
#Fixed permutations 664 second try

#lmao i did something you should not of done but works perfectly with small inputs
#instead of altering the dict after I make it programattically to include "you"
#I just fucked with the input and added "you" to everyone lmaoooo
#640 first try.

#Added the intended way of actually solving part 2 lol