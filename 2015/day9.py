from sys import maxsize 
from itertools import permutations

with open("2015/day9.txt") as text_file:
  text = text_file.read()

locations_list = text.split("\n")

places = set()
distances = {}
for line in locations_list:
  (source, _, dest, _, distance) = line.split()
  places.add(source)
  places.add(dest)
  #If no key, creates key of (Name: {dest:cost}). If there is a key, return the value attached, which is a dictionary with
  #some dest:cost pairs in it. Add a new pair of the current dest:cost. Fucking genius creds to this guy.
  #https://www.reddit.com/r/adventofcode/comments/3w192e/day_9_solutions/cxsix3u/
  distances.setdefault(source, {})[dest] = int(distance) 
  distances.setdefault(dest, {})[source] = int(distance)



shortest = maxsize
longest = 0
for items in permutations(places):
  #Map iterates through both lists evenly, so
  # map(sum, [1, 2, 3, 4], [2, 3, 4, 5]) would return [3, 5, 7, 9] because both list's [0] gets added, then their [1]s and so on
  #Using this, you offset the lists by one each so you dont just return to the same planet you came from for each planet
  #Then you use the distances distionary set up to find the cost of each trip. Example:
  #('Arbre', 'Tristram', 'Faerun', 'Tambi', 'Snowdin', 'AlphaCentauri', 'Straylight')
  #('Tristram', 'Faerun', 'Tambi', 'Snowdin', 'AlphaCentauri', 'Straylight', 'Norrath')
  #[132, 108, 68, 105, 4, 133, 115]
  #Travel from Arbre to Tristram for 132, then Tristram to Faerun for 108, etc. Sum these up to get total cost.
  #Run for each permutation to find lowest overall cost and highest overall cost.
  print(items[:-1])
  print(items[1:])
  print(list(map(lambda x, y: distances[x][y], items[:-1], items[1:])), "\n")
  dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
  shortest = min(shortest, dist)
  longest = max(longest, dist)

print(shortest)
print(longest)
#may not have really solved this one but I learned a lot about .setdefault, set(), and map(). This was useful.