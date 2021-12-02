import re
import itertools
import numpy as np
import time

instructions = open("2021/day2.txt").read().splitlines()

class Sub():
  def __init__(self, position = (0,0)):
    self.x = position[0]
    self.y = position[1]

sub = Sub()

for command in instructions:
  direction = command.split()[0]
  unit = int(command.split()[1])
  if direction == "forward":
    sub.x += unit
  elif direction == "down":
    sub.y += unit
  elif direction == "up":
    sub.y -= unit

print(sub.x * sub.y)
