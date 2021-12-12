import re
import itertools
import numpy as np
import time

instructions = open("2021/day12testinput.txt").read().splitlines()
#instructions = open("2021/day12input.txt").read().splitlines()

class Node():
  def __init__(self, name, paths = []):
    self.name = name
    self.paths = []
    self.big = self.name.isupper()
    self.times_visited = 0
  
  def __repr__(self):
    return self.name
  
  def add_path(self, node):
    self.paths.append(node)
  
  def get_paths(self):
    return self.paths

nodes = {}
for i in instructions:
  start, end = i.split("-")
  if start not in nodes.keys():
    nodes[start] = Node(start)
  if end not in nodes.keys():
    nodes[end] = Node(end)
  nodes[start].add_path(nodes[end])
  nodes[end].add_path(nodes[start])

#run a depth first search on start, and get all possible paths.

def printAllPathsUtil(self, u, d, visited, path):
 
  # Mark the current node as visited and store in path
  visited[u]= True
  path.append(u)

  # If current vertex is same as destination, then print
  # current path[]
  if u == d:
      print path
  else:
      # If current vertex is not destination
      # Recur for all the vertices adjacent to this vertex
      for i in self.graph[u]:
          if visited[i]== False:
              self.printAllPathsUtil(i, d, visited, path)
                
  # Remove current vertex from path[] and mark it as unvisited
  path.pop()
  visited[u]= False

def printAllPaths(self, s, d):
 
  # Mark all the vertices as not visited
  visited =[False]*(self.V)

  # Create an array to store paths
  path = []

  # Call the recursive helper function to print all paths
  self.printAllPathsUtil(s, d, visited, path)