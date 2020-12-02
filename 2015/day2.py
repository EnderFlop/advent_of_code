with open("2015/day2.txt") as text_file:
  text = text_file.read()

dim_list = text.split("\n")
total_feet = 0
for dimensions in dim_list:
  dimensions_split = dimensions.split("x")
  l = int(dimensions_split[0])
  w = int(dimensions_split[1])
  h = int(dimensions_split[2])
  volume = l*w*h
  feet_list = [l,w,h]
  feet_list.sort()
  perimeter = 2*feet_list[0] + 2*feet_list[1]
  total = volume + perimeter
  total_feet += total
  print(l,w,h,volume,perimeter,total,total_feet)
print(total_feet)