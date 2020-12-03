with open("2020/day3.txt") as text_file:
  mountain = text_file.read()

mountain = mountain.split("\n")
#each line is 31 char long
slope_dict = {
  (1,1) : 0,
  (3,1) : 0,
  (5,1) : 0,
  (7,1) : 0,
  (1,2) : 0
}

for slope in slope_dict.keys():
  current_pos = [0,0]
  while current_pos[1] <= len(mountain)-1:
    current_line = mountain[current_pos[1]]
    if current_line[current_pos[0] % 31] == "#":
      slope_dict[slope] += 1
    current_pos[0] += slope[0]
    current_pos[1] += slope[1]
  print(slope_dict[slope])

multiplication = 1
for value in slope_dict.values():
  multiplication *= value
print(multiplication)