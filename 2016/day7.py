import re
import itertools
import numpy as np
import time

instructions = open("2016/day7.txt").read().splitlines()

valid_count = 0

def is_aba(string):
  return string[0] == string[2] and string[0] != string[1]

def scan_for_aba(string):
  i = 0
  abas = []
  while i < len(string) - 2:
    #print(f"scanning {string[i:i+3]}")
    if is_aba(string[i:i+3]):
      abas.append(string[i:i+3])
    i += 1
  if abas:
    return abas
  return False


for string in instructions:
  inside_brackets = re.findall(r"\[\w+\]", string)
  #If there is an aba inside the backets, record it.
  abas = []
  for i in inside_brackets:
    inside_string = i[1:-1]
    result = scan_for_aba(inside_string)
    if result != False:
      abas += result

  #If we found an aba in the brackets
  if abas:
    #make a list of all the "bab"s
    babs = []
    for aba in abas:
      babs.append(aba[1] + aba[0] + aba[1])
    
    #remove the bracketed text
    for i in inside_brackets:
      string = string.replace(i, " ")

    #for the rest of the text, if any of it contains a "bab", it counts.
    other_sequences = string.split()
    found = False
    for bab in babs:
      for sequence in other_sequences:
        if bab in sequence:
          valid_count += 1
          found = True
        if found: #If the sequence is confirmed, don't check anymore
          break
      if found: #If the sequence is confirmed, don't check anymore
        break

print(valid_count)
#part1 113 not right, too high. checked again, guarenteed 113 too high.
#what could be letting an invalid solution through? It must succeed a check it should fail. There is an error somewhere.
#The regex is correct, and so is the string replacement. is_abba() is correct. scan_for_abba() is also correct.
#105!! I did the things where after I removed the bracketed sequences, it made an abba with the smashed together halves.
#Fixed this by replacing them with a space, splitting the string, and running the abba search on each of the tiny sequences

#part2 164 too low.
#part2 258! I had accidentally made it so abas was overwritten everytime a new set was found. Now it just adds all the sequences to the list
#Fun fact, aba and bab are switched around from the notation used in the instruction. whatever lol