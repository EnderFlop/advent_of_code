import re
import itertools
import numpy as np
from collections import defaultdict
instructions = open("2025/day7testinput.txt").read().splitlines()
#instructions = open("2025/day7input.txt").read().splitlines()

#get beam indexes (all | or S in row)
#cast beam beneath (read row below)
#   if index below is a ., turn to a |
#   if index below is a ^, turn left and right into |

beams = {instructions[0].find("S"): 1}

for row_idx in range(1, len(instructions)):
    row = instructions[row_idx]
    new_beams = defaultdict(int)
    for beam, count in beams.items():
        #if empty, turn to beam
        if row[beam] == ".":
            new_beams[beam] += count
        #if splitter, split
        if row[beam] == "^":
            if beam - 1 >= 0:
                new_beams[beam - 1] += count
            if beam + 1 < len(row):
                new_beams[beam + 1] += count
    beams = new_beams

print(sum(beams.values()))
#1546 part1 answer

#13883459503480 part2 answer
# had to pivot from recursive backtracking approach, even memoization couldn't save it