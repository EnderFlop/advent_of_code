input = open("2016/day1.txt").read().splitlines()
input = input[0].split(",")
input = [i.strip() for i in input]
#print(input)



compass = ["N", "E", "S", "W"]
facing = 0
coordinates = [[0,0]]
for direction in input:
  new_coords = coordinates[-1].copy()
  if direction[0] == "R":
    facing += 1
  if direction[0] == "L":
    facing -= 1
  facing_direction = compass[facing%4]
  distance = int(direction[1:])
  if facing_direction == "N":
    for i in range(distance):
      new_coords[1] += 1
      if new_coords in coordinates:
        print(new_coords)
      coordinates.append(new_coords.copy())

  elif facing_direction == "E":
    for i in range(distance):
      new_coords[0] += 1
      if new_coords in coordinates:
        print(new_coords)
      coordinates.append(new_coords.copy())

  elif facing_direction == "S":
    for i in range(distance):
      new_coords[1] -= 1
      if new_coords in coordinates:
        print(new_coords)
      coordinates.append(new_coords.copy())

  elif facing_direction == "W":
    for i in range(distance):
      new_coords[0] -= 1
      if new_coords in coordinates:
        print(new_coords)
      coordinates.append(new_coords.copy())

#print(coordinates)
  
#part1 231 first try!

#part2 215 too high
#not 2
#147! third try
#had a lot of trouble with remembering that lists are mutable lol.