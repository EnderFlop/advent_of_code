import re
import itertools
import numpy as np
import time
import math
import heapq

#instructions = open("2021/day15testinput.txt").read().splitlines()
instructions = open("2021/day15input.txt").read().splitlines()

instructions = [[int(i) for i in x] for x in instructions]
grid = np.asarray(instructions)
#bfs the whole grid to get every path. calculate the sum of the risk of all paths. find the minimum


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

    # function to add an edge to graph
    def addEdge(self, u, v):
      start_coords = str(u)
      if start_coords not in self.graph.keys():
        self.graph[start_coords] = []
      self.graph[start_coords].append(v)
  
    def shortest(self, start, path):
      if start.previous:
        print(start.previous.coords)
        path.append(start.previous.risk)
        self.shortest(start.previous, path)
      return
    
    def dijkstra(self, start, end):
      start.distance = 0
      unvisted_queue = [node for node in nodes.values()]
      heapq.heapify(unvisted_queue)
      while unvisted_queue:
        current_node = heapq.heappop(unvisted_queue)
        current_node.visited = True
        for next_node in self.graph[str(current_node.coords)]:
          if next_node.visited:
            continue
          new_distance = current_node.distance + next_node.risk
          if new_distance < next_node.distance:
            #print(next_node.coords)
            next_node.previous = current_node
            next_node.distance = new_distance
        
        while unvisted_queue:
          heapq.heappop(unvisted_queue)
        unvisted_queue = [node for node in nodes.values() if node.visited == False]
        heapq.heapify(unvisted_queue)

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


graph.dijkstra(nodes[str([0,0])], nodes[str([99,99])])
target = nodes[str([99,99])]
path = [target.risk]
graph.shortest(target, path)
print(sum(path) - nodes[str([0,0])].risk)
#540 first try! amazed that this worked. I used a model of dijkstras algorithm but changed so much to fit my own variables i'm ecstatic that it pulled through.
#takes around thirty seconds to run though, i'm sure there's a faster way of going about it but this functions for now. I hope part 2 doesn't ask anything crazy.