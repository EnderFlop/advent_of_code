import re
import itertools

input = "hxbxwxba"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #No I, O, L

def meets_reqs(string):
  three_letters = False
  for index in range(len(string) - 2):
    check_string = string[index:index+3]
    if alphabet.index(check_string[0]) == alphabet.index(check_string[1]) - 1 and alphabet.index(check_string[0]) == alphabet.index(check_string[2]) - 2:
      three_letters = True
  if three_letters == False:
    return False
  in_a_row = 0
  groups = itertools.groupby(string)
  for k, g in groups:
    if len(list(g)) == 2:
      in_a_row += 1
  if in_a_row == 2:
    return True
  return False

def get_next_letter(string):
  alphabet_index = alphabet.index(string[-1]) #Get the index of the letter in the alphabet list
  if alphabet_index != len(alphabet)-1: #If the letter isnt z
    return string[:-1] + alphabet[alphabet_index + 1] #Return the string with the last letter increased by 1
  return get_next_letter(string[:-1]) + "a" #Rerun the function on the list minus the last character, then add "a"

while True:
  input = get_next_letter(input)
  if meets_reqs(input):
    print(input)
    break