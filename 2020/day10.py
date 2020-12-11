import re
import itertools

with open("2020/day10.txt") as text:
  text = text.read().splitlines()
text = [int(i) for i in text]
text = sorted(text)
text.insert(0, 0)
text.append(text[-1]+3)

paths = {text[index]: 0 for index in range(len(text))}
for key in paths.keys():
  if key == 0:
    paths[key] += 1
  print(f"There are {paths[key]} ways to get to {key}")
  if key+1 in paths.keys():
    paths[key+1] += paths[key]
    print(f"{key+1} is only 1 away from {key}, so all the paths that can reach {key} can also reach {key+1}")
  if key+2 in paths.keys():
    paths[key+2] += paths[key]
    print(f"{key+2} is only 2 away from {key}, so all the paths that can reach {key} can also reach {key+2}")
  if key+3 in paths.keys():
    paths[key+3] += paths[key]
    print(f"{key+3} is only 3 away from {key}, so all the paths that can reach {key} can also reach {key+3}")

print(paths)