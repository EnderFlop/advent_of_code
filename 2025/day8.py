import re
import itertools
import numpy as np
import math

#instructions = open("2025/day8testinput.txt").read().splitlines()
instructions = open("2025/day8input.txt").read().splitlines()

class Junction():
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.connections = set()

  def compare_distance(self, other_junction):
    return math.sqrt(
      ((self.x - other_junction.x) ** 2) +
      ((self.y - other_junction.y) ** 2) +
      ((self.z - other_junction.z) ** 2)
    )
  
  def check_connection(self, other_junction):
    return other_junction in self.connections

  def connect(self, other_junction):
    self.connections.add(other_junction)


  def __repr__(self):
    return f"// {self.x}, {self.y}, {self.z} //\n"

#initialize the junctions

juncs = []

for coords in instructions:
  x, y, z = coords.split(",")
  x, y, z = int(x), int(y), int(z)
  juncs.append(Junction(x, y, z))

#connect the junctions

for x in range(1000):
  print(x)
  minimum_distance = 9999999
  min_juncs = []
  for idx, i in enumerate(juncs):
    for j in juncs[idx + 1:]:
      dist = i.compare_distance(j)
      if dist < minimum_distance and not i.check_connection(j):
        minimum_distance = dist
        min_juncs = [i, j]

  min_juncs[0].connect(min_juncs[1])
  min_juncs[1].connect(min_juncs[0])


#DFS on the junctions to find the pool sizes
complete_circuits = set()
all_counts = []
for i in juncs:
  if i in complete_circuits:
    continue

  visited = set()
  queue = [i]
  count = 0
  while queue:
    current = queue.pop(0)
    if current not in visited:
      count += 1
      visited.add(current)
      queue.extend(current.connections)
  
  for j in visited:
    complete_circuits.add(j)
  
  all_counts.append(count)

all_counts.sort(reverse=True)
result = math.prod(all_counts[:3])
print(result)

#121770 part1 answer