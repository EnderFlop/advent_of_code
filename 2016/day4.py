import re
import itertools
import numpy as np
import time
import string

instructions = open("2016/day4.txt").read().splitlines()

sector_id_sum = 0
alphabet = string.ascii_lowercase

for text in instructions:
  checksum = re.search("\[.+\]", text)
  checksum = checksum.group()[1:-1]
  letter_dict = {k:0 for k in alphabet}
  sector_id = text[-10:-7]
  for letter in text[:-10]:
    if letter == "-":
      pass
    else:
      letter_dict[letter] += 1
    
  #letter dict is now a dictionary with letters as keys and their appearance count in the string as values
  #for each letter in checksum, check if it has greater count than the letter after it. If it has equal count, check that it has a lower alphabetical index that it.

  #five most common letters
  five_most_common = []
  temp_letter_dict = letter_dict.copy()
  while len(five_most_common) != 5:
    largest_value = -1
    largest_letter = "."
    for k, v in temp_letter_dict.items():
      if v > largest_value:
        largest_value = v
        largest_letter = k
    five_most_common.append(largest_letter)
    temp_letter_dict[largest_letter] = -1

  index = 0
  valid_string = True

  while index < 4:
    if not all(letter in checksum for letter in five_most_common):
      valid_string = False
    current_letter = checksum[index]
    next_letter = checksum[index + 1]
    if letter_dict[current_letter] > letter_dict[next_letter]:
      pass
    elif letter_dict[current_letter] == letter_dict[next_letter]:
      if alphabet.index(current_letter) < alphabet.index(next_letter):
        pass
      else:
        valid_string = False
    else:
      valid_string = False
    index += 1
  if valid_string == True:
    sector_id_sum += int(sector_id)

print(sector_id_sum)
#part1 248142 too high. 245102 right! second try.