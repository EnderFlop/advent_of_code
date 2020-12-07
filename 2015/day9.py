import re

with open("2015/day9.txt") as text_file:
  text = text_file.read()

locations_list = text.split("\n")

def reset_visited():
  visited = {}
  for location in locations_list:
    location_title = location.split(" ")[0]
    visited[location_title] = False
  return visited

visited = reset_visited()
locations_dict = {}
for location in locations_list:
  location_title = location.split(" ")[0]
  locations_dict[location_title] = []

for location in locations_list:
  split = location.split(" ")
  locations_dict[split[0]].append((split[2], split[4]))
#We now have a dict. Each key is a location, and each value is a list of tuples of (destination, cost).
def bfs(start):
  queue = []
  total_cost = 0
  queue.append(start)
  visited[start] = True

  while queue:
    current = queue.pop(0)
    print(current)
    total_cost += int(current[1])
    for destination in locations_dict[current[0]]:
      try:
        if visited[destination[0]] == False:
          queue.append(destination)
          visited[destination[0]] = True
      except KeyError:
        visited[destination[0]] = True
  
  print(total_cost)

bfs(("Tambi", 0))