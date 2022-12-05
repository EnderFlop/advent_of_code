import re
import itertools
import numpy as np
import time

#instructions = open("2022/day2testinput.txt").read().splitlines()
instructions = open("2022/day2input.txt").read().splitlines()

winning_dict = {"X": "C", "Y": "A", "Z": "B"}
tie_dict = {"X": "A", "Y": "B", "Z": "C"}
#X (rock) beats C (scissors), Y (paper) beats A (rock), Z (scissors) beats B (paper)

throw_points_dict = {"X": 1, "Y": 2, "Z": 3}
#points :: rock:1, paper:2, scissors:3

total_points = 0
for round in instructions:
  round_points = 0
  enemy, player = round.split(" ")

  #determine round result and points
  if winning_dict[player] == enemy:
    round_points += 6
  elif tie_dict[player] == enemy:
    round_points += 3
  #else, loss, total_points += 0

  #add additional points based on player throw
  round_points += throw_points_dict[player]

  total_points += round_points

print(total_points)
#part1 11906 first try!