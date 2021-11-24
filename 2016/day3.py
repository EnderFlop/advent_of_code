import re
import itertools
import numpy as np
import time

instructions = open("2016/day3.txt").read().splitlines()

valid_triangles = 0
for triangle in instructions:
  side1, side2, side3 = triangle.split()
  side1, side2, side3 = int(side1), int(side2), int(side3)
  if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    valid_triangles += 1
  
#983, second try (forgot to convert to int lol)