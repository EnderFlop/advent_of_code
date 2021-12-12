import re
import itertools
import numpy as np
import time
from collections import defaultdict

#instructions = open("2021/day12testinput.txt").read().splitlines()
instructions = open("2021/day12input.txt").read().splitlines()


# This class represents a directed graph
# using adjacency list representation

class Node():
  def __init__(self, name):
    self.name = name
    self.big = self.name.isupper()
    self.times_visited = 0

  def __repr__(self):
    return self.name

class Graph:
  
    def __init__(self, vertices):
      # No. of vertices
      self.V = vertices
        
      # default dictionary to store graph
      self.graph = {}

      self.path = []

      self.path_count = 0

      self.small_cave_visited = False
  
    # function to add an edge to graph
    def addEdge(self, u, v):
      if u.name not in self.graph.keys():
        self.graph[u.name] = []
      self.graph[u.name].append(v)
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def dfs(self, start, end):

      current_node = nodes[start.name]

      # Mark the current node as visited and store in path
      current_node.times_visited += 1
      self.path.append(current_node)

      # If current vertex is same as destination, then print
      # current path[]
      if start.name == end.name:
        self.path_count += 1
        #print(self.path)
      else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[start.name]:
          i = nodes[i.name]
          # small nodes can only be visited once, big nodes can be visited however often
          if (i.name == "start"):
            continue
          if (i.name == "end" and i.times_visited == 0):
            self.dfs(i, end)
          elif (i.times_visited == 0 and i.big == False):
            self.dfs(i, end)
          elif (i.times_visited == 1 and i.big == False and self.small_cave_visited == False):
            self.small_cave_visited = True
            self.dfs(i, end)
          elif (i.big == True):
            self.dfs(i, end)
      self.path.pop()
      if current_node.times_visited == 2 and current_node.big == False: #if we just removed the small cave 
        self.small_cave_visited = False
      current_node.times_visited -= 1


graph = Graph(len(instructions))
nodes = {}
for i in instructions:
  start, end = i.split("-")
  start = Node(start)
  if start.name not in nodes.keys():
    nodes[start.name] = start
  end = Node(end)
  if end.name not in nodes.keys():
    nodes[end.name] = end
  graph.addEdge(start, end)
  graph.addEdge(end, start)

graph.dfs(nodes["start"], nodes["end"])
print(graph.path_count)
#3856 first try! uses a HEAVILY modified version of the "print all paths" code found here https://www.geeksforgeeks.org/find-paths-given-source-destination/
#116692 first try! had a rough time figuring out how to mark when I had already visited a small cave and when I hadn't 
# i accidentally marked small_cave_visited False when times_visited was 2, even if it was a big cave >:( 
# but I got it in the end!