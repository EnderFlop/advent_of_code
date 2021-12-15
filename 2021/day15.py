import re
import itertools
import numpy as np
import time
import math
import heapq

start = time.time()

#instructions = open("2021/day15testinput.txt").read().splitlines()
instructions = open("2021/day15input.txt").read().splitlines()

instructions = [[int(i) for i in x] for x in instructions]
grid = np.asarray(instructions)
#take the grid, change every number to num + 1, if num == 10 num = 1, slap it on the left and right
original_grid = grid.copy()

for i in range(1, 5): #make the grid vertically
  new_grid = original_grid.copy()
  for row_index, row in enumerate(new_grid):
    for point_index, point in enumerate(row):
      new_grid[row_index][point_index] += i
      if point + i >= 10:
        new_grid[row_index][point_index] = ((point + i) % 10) + 1
  grid = np.concatenate([grid, new_grid], axis=0)

original_grid = grid.copy()
for i in range(1, 5): #make the grid horizontally
  new_grid = original_grid.copy()
  for row_index, row in enumerate(new_grid):
    for point_index, point in enumerate(row):
      new_grid[row_index][point_index] += i
      if point + i >= 10:
        new_grid[row_index][point_index] = ((point + i) % 10) + 1
  grid = np.concatenate([grid, new_grid], axis=1)

#grid is now set up correctly.


class Node():
  def __init__(self, risk, coords):
    self.distance = math.inf
    self.risk = risk
    self.coords = coords
    self.visited = False
    self.previous = None

  def __repr__(self):
    return f"{self.risk} {self.coords}. D:{self.distance}"
  
  def __lt__(self, other):
    return self.distance < other.distance
  
  def __gt__(self, other):
    return self.distance > other.distance

class Graph():
    def __init__(self):
      # default dictionary to store graph
      self.graph = {}

      self.path = []

      self.path_count = 0

      self.shortest_path = []

    # function to add an edge to graph
    def addEdge(self, u, v):
      start_coords = str(u)
      if start_coords not in self.graph.keys():
        self.graph[start_coords] = []
      self.graph[start_coords].append(v)
  
    
    def dijkstra(self, start, end):
      start.distance = 0
      end_coords = str(end.coords)
      unvisted_queue = [start]
      heapq.heapify(unvisted_queue)
      while unvisted_queue:

        current_node = heapq.heappop(unvisted_queue)
        current_node.visited = True
        current_node_coords = str(current_node.coords)

        if current_node_coords == end_coords:
          self.shortest_path.append(current_node.risk)
          while current_node.previous:
            self.shortest_path.append(current_node.previous.risk)
            current_node = current_node.previous
          return

        for next_node in self.graph[str(current_node.coords)]:
          new_distance = current_node.distance + next_node.risk
          if next_node.visited:
            continue
          elif new_distance < next_node.distance:
            #print(next_node.coords)
            next_node.previous = current_node
            next_node.distance = new_distance
            heapq.heappush(unvisted_queue, next_node)
          

graph = Graph()

def find_neighbors(grid, row_index, point_index): #shamelessly stolen from MYSELF HAHA (day11 2020)
  slopes = [(0,-1), (-1,0), (1,0), (0,1),] #The slopes to check
  for slope in slopes:
    current_pos = [row_index, point_index]
    current_pos[0] += slope[0] #Move by x of slope
    current_pos[1] += slope[1] #Move by y of slope
    if current_pos[0] < 0 or current_pos[0] >= len(grid) or current_pos[1] < 0 or current_pos[1] >= len(grid[row_index]): #if it is out of bounds, skip
      continue
    else:
      graph.addEdge(str([row_index, point_index]), nodes[str([current_pos[0], current_pos[1]])])

nodes = {}
for row_index, row in enumerate(grid): #once to initalize all the nodes in nodes
  for point_index, point in enumerate(row):
    coords = str([row_index, point_index])
    nodes[coords] = Node(point, coords)

for row_index, row in enumerate(grid): #once to find all the neighbors and add their edges to the graph
  for point_index, point in enumerate(row):
    find_neighbors(grid, row_index, point_index)


graph.dijkstra(nodes[str([0,0])], nodes[str([499,499])])
target = nodes[str([499,499])]

#graph.dijkstra(nodes[str([0,0])], nodes[str([49,49])])
#target = nodes[str([49,49])]

print("\n")
print(sum(graph.shortest_path) - nodes[str([0,0])].risk)
#540 first try! amazed that this worked. I used a model of dijkstras algorithm but changed so much to fit my own variables i'm ecstatic that it pulled through.
#takes around thirty seconds to run though, i'm sure there's a faster way of going about it but this functions for now. I hope part 2 doesn't ask anything crazy.

#progress! I've expanded the grid correctly and it workes on the new sample input. my implimentation of dijkstra's is far too slow to be run in any decent amount of time
#I am going to bed, but I will run the algorithm while I sleep and hope for a result in the morning :)
end = time.time()
print(end - start)
#2879! just had to optimize the algorithm a little bit. turns out the first one I found was pretty terrible.
#this source helped me out a ton https://codereview.stackexchange.com/questions/235898/speeding-up-dijkstras-algorithm
