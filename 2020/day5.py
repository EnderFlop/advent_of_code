import re

with open("2020/day5.txt") as text_file:
  directions = text_file.read()

directions = directions.split("\n")
#directions = ["FBFBBFFRLR"]
seats_list = [row * 8 + column for row in range(0,127) for column in range(0,8)]
empty_seats = []
print(seats_list)
for direction in directions:
  row = [0,127]
  final_row = 0
  column = [0,7]
  final_col = 0
  #print(row, column)
  for index in range(len(direction)): 
    row_diff = (row[1] - row[0]) + 1
    col_diff = (column[1] - column[0]) + 1
    if direction[index] == "B":
      row[0] += row_diff // 2
      final_row = row[0]
    elif direction[index] == "F":
      row[1] -= row_diff // 2
      final_row = row[1]
    elif direction[index] == "R":
      column[0] += col_diff // 2
      final_col = column[0]
    elif direction[index] == "L":
      column[1] -= col_diff // 2
      final_col = column[1]
    #print(row, column)
  seat_id = final_row * 8 + final_col
  #print(final_row, final_col, seat_id)
  seats_list.remove(seat_id)
print(seats_list)
#Answer is 552