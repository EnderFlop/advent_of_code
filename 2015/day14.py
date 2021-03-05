import itertools
import re

with open("2015/day14.txt") as text_file:
  text = text_file.read().splitlines()

#text = "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\nDancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.".splitlines()
#reindeer is a dict of reindeer to their current distance.
reindeer = {}
seconds = {}
for r in text:
  numbers = re.findall("\d+", r)
  reindeer[r.split()[0]] = {
  "distance":0, 
  "speed":int(numbers[0]),
  "flight_time":int(numbers[1]),
  "rest_time":int(numbers[2])}

# 1 % 127 < 10

print(reindeer)
for current_second in range(2503):
  for rein, attributes in reindeer.items():
    if current_second % (attributes["rest_time"] + attributes["flight_time"]) < attributes["flight_time"]:
      attributes["distance"] += attributes["speed"]

for n, i in reindeer.items():
  print(n, i["distance"])

#2660 first try!