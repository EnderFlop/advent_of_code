import re
import itertools
import numpy as np
import time

instructions = open("2016/day7.txt").read().splitlines()

valid_count = 0

def is_abba(string):
  return string[0] == string[3] and string[1] == string[2] and string[0] != string[1]

def scan_for_abba(string):
  i = 0
  while i < len(string) - 3:
    if is_abba(string[i:i+4]):
      return True
    i += 1
  return False

for string in instructions:
  sequence_in_brackets = False
  sequence_in_regular = False
  inside_brackets = re.findall(r"\[\w+\]", string)
  #If there is an abba inside brackets, it fails instantly
  for i in inside_brackets:
    inside_string = i[1:-1]
    if scan_for_abba(inside_string):
      sequence_in_brackets = True
  #else, test for an abba outside the backets. if there isn't one, also fails
  #remove the bracketed text
  for i in inside_brackets:
    string = string.replace(i, " ")
  other_sequences = string.split()
  for sequence in other_sequences:
    if scan_for_abba(sequence):
      sequence_in_regular = True

  if not sequence_in_brackets and sequence_in_regular:
    print(f"valid_string found! {string}\n")
    valid_count += 1

print(valid_count)
#part1 113 not right, too high. checked again, guarenteed 113 too high.
#what could be letting an invalid solution through? It must succeed a check it should fail. There is an error somewhere.
#The regex is correct, and so is the string replacement. is_abba() is correct. scan_for_abba() is also correct.
#105!! I did the things where after I removed the bracketed sequences, it made an abba with the smashed together halves.
#Fixed this by replacing them with a space, splitting the string, and running the abba search on each of the tiny sequences