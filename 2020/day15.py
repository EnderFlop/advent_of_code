import re
import itertools
from rich.traceback import install
from rich.console import Console
install()
console = Console()

input = [0,3,6]
said_dict = {i: [0,0] for i in input} #KEY is number spoken, KEY[0] is most recent turn spoken, KEY[1] is most recent turn before that.
def read_number(last_number, turn):
  console.log(f"The last number read was {last_number}.")
  if last_number in said_dict: #If it has been spoken before
    console.log(f"It has been said before")
    turns = said_dict[last_number] 
    console.log(f"The last two times this was said were {turns[0]} and {turns[1]}")
    difference = turns[0] - turns[1] #Difference between the most recent speaking and the most recent before that
    console.log(f"returning {turns[0]} - {turns[1]} ({difference})")
    turns[0], turns[1] = turn, turns[0] #Set [0] to the most recent turn and [1] to the turn before it (the one stored in 0)
    return difference
  else: #If it hasn't been spoken before
    console.log(f"It HASN'T been said before")
    said_dict[last_number] = [turn, 0] #Create a new key with [0] set as the current turn
    console.log(said_dict[last_number])
    return 0 #First time number is spoken player says 0

def read_starters(turn):
  console.log(f"Initalizing {input[turn-1]} to {[turn, 0]}")
  said_dict[input[turn-1]] = [turn, 0]

for turn in range(10):
  turn = turn+1 #Turn starts at 1
  console.log(turn)
  if turn <= len(input): #For the first x numbers, read that number
    read_starters(turn)
    last_number = input[turn-1]
  else: #Otherwise, read the last read number
    last_number = read_number(last_number, turn) 
print(last_number)