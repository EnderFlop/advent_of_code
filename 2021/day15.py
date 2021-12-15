import re
import itertools
import numpy as np
import time

instructions = open("2021/day15testinput.txt").read().splitlines()
#instructions = open("2021/day15input.txt").read().splitlines()

instructions = [[int(i) for i in x] for x in instructions]
grid = np.asarray(instructions)
#bfs the whole grid to get every path. calculate the sum of the risk of all paths. find the minimum


class Node():
  def __init__(self, risk, coords):
    self.risk = risk
    self.coords = coords
    self.times_visited = 0

  def __repr__(self):
    return f"{self.risk} {self.coords}"

class Graph():
    def __init__(self):
      # default dictionary to store graph
      self.graph = {}

      self.path = []

      self.path_count = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
      start_coords = str(u)
      if start_coords not in self.graph.keys():
        self.graph[start_coords] = []
      self.graph[start_coords].append(v)
  
    def dfs(self, start, end):
      start_coords = str(start.coords)
      current_node = nodes[start_coords]

      # Mark the current node as visited and store in path
      current_node.times_visited += 1
      self.path.append(current_node)

      # If current vertex is same as destination, then print
      # current path[]
      if start.coords == end.coords:
        #print(self.path)
        all_paths.append(self.path)
      else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[start_coords]:
          i = nodes[str(i.coords)]
          if (i.times_visited == 0):
            self.dfs(i, end)
      self.path.pop()
      current_node.times_visited -= 1
      if len(all_paths) % 100000 == 0:
        print(len(all_paths))

graph = Graph()

def find_neighbors(grid, row_index, point_index): #shamelessly stolen from MYSELF HAHA (day11 2020)
  slopes = [(-1, -1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)] #The slopes to check
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

all_paths = []
graph.dfs(nodes[str([0,0])], nodes[str([9,9])])