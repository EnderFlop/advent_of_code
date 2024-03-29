import re
import itertools
import time
from rich.traceback import install
from rich.console import Console
install()
console = Console()

input = [2,0,1,7,4,14,18]
said_dict = {i: [0,0] for i in input} #KEY is number spoken, KEY[0] is most recent turn spoken, KEY[1] is most recent turn before that.

def read_number(last_number, turn):
  turns = said_dict[last_number] #Get the most recent times the number has been spoken

  if turns[0] == turn-1 and turns[1] == 0: #If it was the first time it's been said
    if 0 in said_dict:
      said_dict[0] = [turn, said_dict[0][0]] #Say 0 and update when 0 was said
    else:
      said_dict[0] = [turn, 0]
    return 0
   
  else:
    difference = turns[0] - turns[1] #Find the difference
    if difference in said_dict:
      said_dict[difference] = [turn, said_dict[difference][0]]
    else:
      said_dict[difference] = [turn, 0]
    return difference
  #If the number has been spoken before
    #Speak most recent - 2nd most recent and update when that number has been spoken

def read_starters(turn):
  said_dict[input[turn-1]] = [turn, 0]

start_time = time.time()
turn_count = 30000000
console.log(f"STARTING. SIMULATING {turn_count} TURNS.")
for turn in range(turn_count):
  turn = turn+1
  if turn <= len(input): #For the first x numbers, read that number
    read_starters(turn)
    last_number = input[turn-1]
  else: #Otherwise, read the last read number
    last_number = read_number(last_number, turn) 
console.log(last_number)
console.log(f"IT TOOK {time.time() - start_time} SECONDS")

#PART 1: 496 FIRST TRY
#PART 2: 883 FIRST TRY
#Ran part 2 in 52 seconds! I think this is O(n) but I'm not sure.
#Obviously the input is the number of turns, and it iterates through those one at a time
#but the length of the input is never used in any of the functions. I'm confident this is O(n)