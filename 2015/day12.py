import itertools
import re
import json

with open("2015/day12.txt") as text_file:
  text = json.load(text_file)

class Sum():
  def __init__(self):
    self.total = 0

  def add_inside(self, data):
    if isinstance(data, int):
      self.total += data
    elif isinstance(data, list):
      for i in data:
        self.add_inside(i)
    elif isinstance(data, dict):
      for k,v in data.items():
        if isinstance(k, int):
          self.total += k
        if isinstance(v, int):
          self.total += v
        if isinstance(v, list):
          for item in v:
            self.add_inside(item)
        if isinstance(v, dict):
          self.add_inside(v)

part1 = Sum()
part1.add_inside(text)
print(part1.total)

#NOT 19835 FOR PART 1, ANSWER TOO LOW
#NOT 2200320 EITHER, TOO HIGH
#119433 FOR PART 1! 3RD TRY