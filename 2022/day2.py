import re
import itertools
import numpy as np
import time

#instructions = open("2022/day2testinput.txt").read().splitlines()
instructions = open("2022/day2input.txt").read().splitlines()

winning_dict = {"A": "Y", "B": "Z", "C": "X"}
tie_dict = {"A": "X", "B": "Y", "C": "Z"}
lose_dict= {"A": "Z", "B": "X", "C": "Y"}
#X (rock) beats C (scissors), Y (paper) beats A (rock), Z (scissors) beats B (paper)

throw_points_dict = {"X": 1, "Y": 2, "Z": 3}
#points :: rock:1, paper:2, scissors:3

total_points = 0
for round in instructions:
  round_points = 0
  enemy, player = round.split(" ")

  #determine player throw
  if player == "X": #lose
    player_throw = lose_dict[enemy]
  elif player == "Y":
    player_throw = tie_dict[enemy]
    round_points += 3 
  else:
    player_throw = winning_dict[enemy]
    round_points += 6

  #add additional points based on player throw
  round_points += throw_points_dict[player_throw]
  #print(round_points)

  total_points += round_points

print(total_points)
#part1 11906 first try!
#part2 11186 first try!