import re
import itertools
import numpy as np
import time

instructions = open("2021/day2.txt").read().splitlines()

class Sub():
  def __init__(self, position = (0,0)):
    self.x = position[0]
    self.y = position[1]
    self.aim = 0

sub = Sub()

for command in instructions:
  direction = command.split()[0]
  unit = int(command.split()[1])
  if direction == "forward":
    sub.x += unit
    sub.y += sub.aim * unit
  elif direction == "down":
    sub.aim += unit
  elif direction == "up":
    sub.aim -= unit
  #print(sub.x, sub.y, sub.aim)

print(sub.x * sub.y)

#part1 1882980, second try because I got down and up confused and submitted a negative.
#part2 1971232560, second try because I multiplied sub.aim by sub.x instead of unit.
#both mistakes that would have been easily caught if I was not focusing on speed.
#If i tried this on the test examples I would have easily got two first tries. Instead I got it in around seven minutes