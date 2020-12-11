import re
import itertools

board = open("2020/day11.txt").read()
lines = board.splitlines()

class MyList(list):
  def get(self, index):
    return self[index] if len(self) > index else "."

def step(text):
  for row in text:
    row_list = MyList(row)
    for seat_index in range(len(row)):
      seat = row[seat_index]
      if seat == ".":
        pass
      #  xxx  to find seats with respect to o,
      #  xox  1 row higher - 1, 1 row higher, 1 row higher + 1, index-1, index+1, 1 row lower - 1, 1 row lower, 1 row lower + 1
      #  xxx
      # To find 1 row higher, line index - 1, * len(line) to find index, subtract 1 to go back one space
      adjacent_seats = []
      #Add functionality to get row 1 higher and 1 lower. If they dont exist, then the row is just a row of periods.
      #Maybe make board into MyList so you can use the same get method?
      #Maybe make a new class that will return a list of "." the len of row so you can use that instead?
      adjacent_seats.append(row_list.get(seat_index-1))
      adjacent_seats.append(row_list.get(seat_index))
      adjacent_seats.append(row_list.get(seat_index+1))
      #Currently prints the surrounding seats for every single seat. Just need to add the seats above and below, then we can start grouping and calculating
      print(adjacent_seats)

step(lines)
