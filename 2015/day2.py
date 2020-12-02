with open("2015/day2.txt") as text_file:
  text = text_file.read()

dim_list = text.split("\n")
total_square_feet = 0
for dimensions in dim_list:
  dimensions_split = dimensions.split("x")
  l = int(dimensions_split[0])
  w = int(dimensions_split[1])
  h = int(dimensions_split[2])
  surface_area = 2*l*w + 2*w*h + 2*h*l
  feet_list = [l,w,h]
  feet_list.sort()
  slack = feet_list[0] * feet_list[1]
  total = surface_area + slack
  total_square_feet += total
  print(l,w,h,surface_area,slack,total)
print(total_square_feet)