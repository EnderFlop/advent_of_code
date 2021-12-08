import re
import itertools
import numpy as np
import time

#instructions = open("2021/day8tinyinput.txt").read().splitlines()
#instructions = open("2021/day8testinput.txt").read().splitlines()
instructions = open("2021/day8input.txt").read().splitlines()

class SevenSwitch():
  def __init__(self):
    #Seven Switch represented by this.
    #  000
    # 1   5
    # 1   5
    #  222
    # 3   6
    # 3   6
    #  444
    self.value_dict = {i:[] for i in range(7)}
    #the value_dict will have seven slots, each containing a list of possible letters for that slot.
    #if it is certain that the letter is assigned to that slot, it will turn into a str of that single letter

  def __repr__(self):
    return str(self.value_dict)

  def add_letters(self, index_list, characters):
    for index in index_list:
      if type(characters) == list:
        self.value_dict[index] += characters
      else:
        self.value_dict[index] += [c for c in characters]
  
  def give_number(self, letters):
    #have to manually program what indexes lead to what numbers.
    #given a str of letters, turn them into the indexes they light up.
    letters_to_index = {v[0]:k for k, v in self.value_dict.items()}
    index_list = [letters_to_index[letter] for letter in letters]
    switches_on = len(index_list)
    if switches_on == 2:
      return "1"
    elif switches_on == 3:
      return "7"
    elif switches_on == 4:
      return "4"
    elif switches_on == 7:
      return "8"
    elif all(index in index_list for index in [0, 1, 3, 4, 6, 5]):
      return "0"
    elif all(index in index_list for index in [0, 1, 2, 3, 4, 6]):
      return "6"
    elif all(index in index_list for index in [0, 1, 2, 5, 6, 4]):
      return "9"
    elif all(index in index_list for index in [0, 5, 2, 3, 4]):
      return "2"
    elif all(index in index_list for index in [0, 5, 2, 6, 4]):
      return "3"
    elif all(index in index_list for index in [0, 1, 2, 6, 4]):
      return "5"
    print(index_list)
    return "ERROR"

total_output = 0
for i in instructions:
  #this is one set of random flickering
  signal_patterns = i.split("|")[0].split()
  signal_patterns.sort()
  output_values = i.split("|")[1].split()

  seven = SevenSwitch()

  #there is a single "1" pattern in every single input (tested)
  for i in [i for i in signal_patterns if len(i) == 2]:
    ones_options = [x for x in i]
  seven.add_letters([5,6], ones_options)
  #there is a "7" pattern in every single input (tested)
  for i in [i for i in signal_patterns if len(i) == 3]:
    seven_options = [x for x in i]
    for letter in ones_options: #remove where 1 overlaps with 7
      seven_options.remove(letter)
  seven.add_letters([0], seven_options)
  #there is a "4" pattern in every single input (tested)
  for i in [i for i in signal_patterns if len(i) == 4]:
    four_options = [x for x in i]
    for letter in ones_options: #remove where 1 overlaps with 4
      four_options.remove(letter)
  seven.add_letters([1,2], four_options)
  #there is an "8" pattern in every single input (tested)
  for i in [i for i in signal_patterns if len(i) == 7]:
    eight_options = [x for x in i]
    for letter in ones_options: #remove where the other numbers overlap with 8
      eight_options.remove(letter)
    for letter in seven_options:
      eight_options.remove(letter)
    for letter in four_options:
      eight_options.remove(letter)
  seven.add_letters([3,4], eight_options)

  #this finishes implimenting the certain numbers. every slot now has two possible digits, except for the top ("zero" index) having a certain one.
  #now must deal with 6 and 9 (length 6) and 5, 2, 3 (length 5)
  #figure out which characters share indexes, then "add" and "subtract" them to become certain. kinda like picross
    #  000
    # 1   5
    # 1   5
    #  222
    # 3   6
    # 3   6
    #  444
  # (english words used to represent index number, numeral used to represent actual picture of numeral)

  # for both possibilites of what 1 can be, 5 only has one of them.
  # for number in five_length_numbers:
  for signal in [i for i in signal_patterns if len(i) == 5]:
    # out of the possibilities for 1 (indexes five and six), 5 only has one of them.
    possible_letters_to_make_up_one = seven.value_dict[6]
    number_of_matching_letters = 0
    for letter in signal:
      if letter in possible_letters_to_make_up_one:
        number_of_matching_letters += 1
    # if number contains both possibilities for 1, that number is 3.
    if number_of_matching_letters == 2:
      letters_in_index_two = seven.value_dict[2]
      for letter in letters_in_index_two:
        if letter in signal:
          seven.value_dict[2] = letter
        if letter not in signal:
          seven.value_dict[1] = [letter]
      continue
    # we have a 5 and a 2 left.
    letters_in_index_three = seven.value_dict[3]
    number_of_matching_letters = 0
    for letter in signal:
      if letter in letters_in_index_three:
        number_of_matching_letters += 1
    # if number contains both letters in indexes three and four, that number is 2 (since 5 doesnt contain index three)
    if number_of_matching_letters == 2:
      continue
    # WE HAVE THE NUMBER 5.
    # index six is now certain (the letter 5 has), and index five is as well by process of elemination
    for letter in possible_letters_to_make_up_one:
      if letter in signal:
        seven.value_dict[6] = [letter]
      if letter not in signal:
        seven.value_dict[5] = [letter]
    # we can also deduce that since 5 doesnt contain index three and the possibilities for three and four are the same, index four is whatever 5 has.
    for letter in letters_in_index_three:
      if letter in signal:
        seven.value_dict[4] = [letter]
      if letter not in signal:
        seven.value_dict[3] = [letter]
    break #have to break once five is found in order to stop more signals from working on changed possible letters.
  
  #now all we have to do is figure out the one and two index!
  #3 is the only number that doesn't have both one and two. 
  #we can't use our current implimentation above because once the process finds a 5, it stops. let's just search again for a three.
  for signal in [i for i in signal_patterns if len(i) == 5]:
    one_letters = seven.value_dict[5] + seven.value_dict[6]
    number_of_matching_letters = 0
    for letter in signal:
      if letter in one_letters:
        number_of_matching_letters += 1
    # if number contains both possibilities for 1, that number is 3.
    if number_of_matching_letters == 2:
      letters_in_index_two = seven.value_dict[2]
      for letter in letters_in_index_two:
        if letter in signal:
          seven.value_dict[2] = [letter]
        if letter not in signal:
          seven.value_dict[1] = [letter]
  
  #i know this is kinda ugly, but it's 12:33 am on a tuesday night (wednesday morning?)
  #plus it works, which is good enough for advent of code.
  #we now have a gaurentee for what letter goes to which index! now, we feed the switch a set of letters and get back a number.
  
  return_number = "" # i know its a str relax.
  for o in output_values:
    return_number += seven.give_number(o)
  print(return_number)
  total_output += int(return_number)
  
print(total_output)

#416 part1 first try
#1043697 part2 first try. this was incredible. i wasn't expecting to code for two hours straight, but one ms paint drawing later its 12:51 AM.
#feeling very accomplished. i have a feeling there will be a steep dropoff in terms of people who finished both parts.
#I can't imagine anyone has an elegant solution to this. I'm sure there will be much better ones than mine, but still. no one liners here.
#person in first managed to get both stars in 7 minutes, but number 100 was 20:51. 
#I managed 871 for the first part (new record!), and 5477 for the second with a total time of 1:50:32.