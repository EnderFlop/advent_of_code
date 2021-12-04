import re
import itertools
import numpy as np
import time

instructions = open("2021/day4.txt").read().splitlines()
called_numbers = [int(x) for x in instructions[0].split(",")]

class Board():
  def __init__(self, rows):
    grid = []
    for row in rows:
      row = row.split()
      row = [Number(x) for x in row]
      grid.append(row)
    self.grid = np.asarray(grid)
  
  def __repr__(self):
    return f"{self.grid}"
  
  def check_for_win(self):
    #scan all columns, rows (diagonals dont count!)
    for index in range(len(self.grid)):
      row = self.grid[index,:]
      column = self.grid[:,index]
      return all(x.is_called() for x in row) or all(y.is_called() for y in column)
  
  def sum_unmarked_numbers(self):
    unmarked_sum = 0
    for row in self.grid:
      for number in row:
        if number.is_called() == False:
          unmarked_sum += number.get_value()
    return unmarked_sum
  
  def search_for_number(self, value):
    for row in self.grid:
      for number in row:
        if number.get_value() == value:
          number.call()


class Number():
  def __init__(self, value):
    self.value = int(value)
    self.called = False
  
  def __repr__(self):
    if self.called:
      return f"*{self.value}*"
    return f"{self.value}"
  
  def call(self):
    self.called = True
  
  def is_called(self):
    return self.called
  
  def get_value(self):
    return self.value

boards_list = []
for index in range(2, len(instructions[2:]), 6):
  boards_list.append(Board(instructions[index:index+5]))

def run_game():
  for number in called_numbers:
    for board in boards_list:
      board.search_for_number(number)
      if board.check_for_win():
        print("game won!")
        print([board.check_for_win() for board in boards_list])
        return number * board.sum_unmarked_numbers()

print(run_game())
#74981 too high.