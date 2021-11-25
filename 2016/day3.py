import re
import itertools
import numpy as np
import time

instructions = open("2016/day3.txt").read().splitlines()

fake_array = []
for row in instructions:
  side1, side2, side3 = row.split()
  side1, side2, side3 = int(side1), int(side2), int(side3)
  fake_array.append([side1, side2, side3])

triangle_map = np.asarray(fake_array)
valid_triangles = 0

y_pointer = 0
while y_pointer < len(triangle_map):
  for x_pointer in range(3):
    side1, side2, side3 = triangle_map[y_pointer][x_pointer], triangle_map[y_pointer + 1][x_pointer], triangle_map[y_pointer + 2][x_pointer]
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
      valid_triangles += 1
  y_pointer += 3

print(valid_triangles)

#part1 983, second try (forgot to convert to int lol)
#part2 1836, first try! Array manipulation is actually kinda fun lol. surprised I got the pointer math right the first try