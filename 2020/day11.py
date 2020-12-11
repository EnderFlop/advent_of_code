import re
import itertools

board = open("2020/day11.txt").read()
lines = board.splitlines()

board = "...\n.L.\n..."
lines=board.splitlines()

def step(text):
  for row in range(len(text)):
    for index in range(len(text[row])):
      line = text[row]
      seat = line[index]
      if seat == ".":
        continue
      #  xxx  to find seats with respect to o,
      #  xox  1 row higher - 1, 1 row higher, 1 row higher + 1, index-1, index+1, 1 row lower - 1, 1 row lower, 1 row lower + 1
      #  xxx
      # To find 1 row higher, line index - 1, * len(line) to find index, subtract 1 to go back one space
      higher_seats = []
      middle_seats = []
      lower_seats = []
      try:
        higher_seats.append(board[((row-1) * len(line)) - 1])
      except IndexError:
        higher_seats.append(".")
      try:
        higher_seats.append(board[((row-1) * len(line))])
      except IndexError:
        higher_seats.append(".")
      try:
        higher_seats.append(board[((row-1) * len(line)) + 1])
      except IndexError:
        higher_seats.append(".")
      try:
        middle_seats.append(board[((row) * len(line)) - 1])
      except IndexError:
        middle_seats.append(".")
      try:
        middle_seats.append(board[((row) * len(line)) + 1])
      except IndexError:
        middle_seats.append(".")
      try:
        lower_seats.append(board[((row+1) * len(line)) - 1])
      except IndexError:
        lower_seats.append(".")
      try:
        lower_seats.append(board[((row+1) * len(line))])
      except IndexError:
        lower_seats.append(".")
      try:
        lower_seats.append(board[((row+1) * len(line)) + 1])
      except IndexError:
        lower_seats.append(".")
      adjacent_seats = higher_seats + middle_seats + lower_seats
      print(adjacent_seats)

for i in range(len(board)):
  step(lines)
