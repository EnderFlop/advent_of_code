import itertools
import re

with open("2015/day14.txt") as text_file:
  text = text_file.read().splitlines()

#text = "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\nDancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.".splitlines()

reindeers = []
class Reindeer:
  def __init__(self, name, numbers):
    self.name = name
    self.distance = 0
    self.points = 0
    self.speed = int(numbers[0])
    self.flight_time = int(numbers[1])
    self.rest_time = int(numbers[2])

for r in text:
  numbers = re.findall("\d+", r)
  reindeers.append(Reindeer(r.split()[0], numbers))

for current_second in range(2503):
  for doe in reindeers:
    if current_second % (doe.rest_time + doe.flight_time) < doe.flight_time:
      doe.distance += doe.speed
  max_list = []
  furthest_distance = max(d.distance for d in reindeers)
  for doe in reindeers:
    if doe.distance == furthest_distance:
      max_list.append(doe)
  #print(current_second, [r.name for r in max_list])
  for doe in max_list:
    doe.points += 1


max_points = float("-inf")
for doe in reindeers:
  print(doe.name, doe.points)
  if doe.points > max_points:
    max_points = doe.points

print(max_points)
#2660 first try!

#Part 2. 651 too low.
#Part 2. After completely restructuring into a class system, 1256 is the right answer second try.