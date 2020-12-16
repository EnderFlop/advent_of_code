import re
import itertools
from rich.traceback import install
from rich.console import Console
install()
console = Console()

input = [0,3,6]
said_dict = {i: [0,0] for i in input} #KEY is number spoken, KEY[0] is most recent turn spoken, KEY[1] is most recent turn before that.

def read_number(last_number, turn):
  if last_number in said_dict:
    turns = said_dict[last_number] #[last turn said, 2nd last turn said]
    said_dict[last_number] = [turn-1, turns[0]] #Set number to [last turn, most recent call before that]
    console.log(said_dict[last_number])

    #TODO
    #It's got something to do with the order turns and said_dict get assigned
    #One function uses turns if it's assigned before said_dict, the other one uses the other?
    #Unsure if said_dict[last_number] is even being set correctly, especially for the starting numbers

    if turns[0] == turn-1 and turns[1] == 0: #If it was the first time it's been said
      said_dict[0] = [turn, said_dict[0][0]] #Say 0 and update when 0 was said
      return 0

    else: #If it's been said but it's not the first time
      difference = turns[0] - turns[1] #Get the return value
      return difference

  else: #If the last number hadn't been said before
    said_dict[last_number] = [turn-1, 0] #Create a value and set it's most recent call to last turn
    said_dict[0] = [turn, said_dict[0][0]] #Change 0's most recent calls
    return 0

def read_starters(turn):
  said_dict[input[turn-1]] = [turn, 0]

for turn in range(10):
  turn = turn+1
  if turn <= len(input): #For the first x numbers, read that number
    read_starters(turn)
    last_number = input[turn-1]
  else: #Otherwise, read the last read number
    last_number = read_number(last_number, turn) 
print(last_number)