with open("2015/day6.txt") as text_file:
  instructions = text_file.read()

#Init light grid
light_grid = {}
for x in range(1000):
  for y in range(1000):
    light_grid[(x,y)] = 0

instructions = instructions.split("\n")
#instructions = ["turn on 0,0 through 999,999", "turn off 0,0 through 999,999", "toggle 0,0 through 999,999"]
for instruction in instructions:
  instruction = instruction.split()
  if instruction[0] == "toggle":
    command = "toggle"
    instruction = instruction[1:]
  if instruction[1] == "on":
    command = "on"
    instruction = instruction[2:]
  if instruction[1] == "off":
    command = "off"
    instruction = instruction[2:]
  first_x, first_y = instruction[0].split(",")
  second_x, second_y = instruction[2].split(",")
  first_x, first_y, second_x, second_y = int(first_x), int(first_y), int(second_x), int(second_y)
  #print(f"{command} {first_x},{first_y} through {second_x},{second_y}")
  if command == "on":
    for x in range(first_x, second_x + 1):
      for y in range(first_y, second_y + 1):
        #print(f"turning {(x,y)} on")
        light_grid[(x,y)] += 1
  elif command == "off":
    for x in range(first_x, second_x + 1):
      for y in range(first_y, second_y + 1):
        if light_grid[(x,y)] != 0:
          light_grid[(x,y)] -= 1
  elif command == "toggle":
    for x in range(first_x, second_x + 1):
      for y in range(first_y, second_y + 1):
        light_grid[(x,y)] += 2

brightness = 0
for value in light_grid.values():
  brightness += value
print(brightness)