from inspect import stack
import re
import itertools
import numpy as np
import time

#instructions = open("2022/day5testinput.txt").read().splitlines()
instructions = open("2022/day5input.txt").read().splitlines()

#three sections: the blocks, the indexes, and the moves

#get easy stuff
stack_indexes = instructions[instructions.index("") - 1:instructions.index("")][0]
blocks = instructions[:instructions.index(stack_indexes)]
moves = instructions[instructions.index("") + 1:]

#init stack structure
stack_indexes = stack_indexes.replace(" ", "")
stack_range = range(int(stack_indexes[0]), int(stack_indexes[-1]) + 1)
all_stacks = [ [] for i in stack_range]

#move blocks onto stacks
for row in blocks:
  i = 0
  while i < len(row):
    block_val = row[i + 1]
    if block_val != " ":
      all_stacks[i // 4].append(block_val)
    i += 4

# all_stacks is now a list of lists, each representing a stack of blocks from top to bottom.

def interpret_move(move):
  return [int(x) for x in re.findall("\d+", move)]

for move in moves:
  block_count, si1, si2 = interpret_move(move)
  blocks = all_stacks[si1 - 1][0: block_count]
  all_stacks[si1 - 1] = all_stacks[si1 - 1][block_count:]
  all_stacks[si2 - 1] = blocks + all_stacks[si2 - 1]
  #still ugly and unreadable but i went another day without drawing memory diagrams and box n arrow graphs, so it's worth it.

print("".join([stack[0] for stack in all_stacks]))
#part1 ZSQVCCJLL first try!
#part2 QZFJRWHGS first try!