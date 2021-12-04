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
    win = False
    for index in range(len(self.grid)):
      row = self.grid[index,:]
      column = self.grid[:,index]
      win = all(x.is_called() for x in row) or all(y.is_called() for y in column)
      if win:
        break
    return win
    
  
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
    #keep going until there is only one board that isn't true
    winning_list = [board.check_for_win() for board in boards_list]
    if winning_list.count(False) == 1:
      print([index for index, board in enumerate(boards_list) if board.check_for_win() == False])
      #board index 13
    if boards_list[13].check_for_win():
      return number * boards_list[13].sum_unmarked_numbers()

print(run_game())

#74981 too high. 33363 also too high.
#part1 4662. I had to use someone elses answer to see a demonstration of my boards. 
# My return statement was returning after the first column/row, and not scanning the others. Fixed it.

#part2 4158 too low
#answer had to be once the board did eventually win. Final answer 12080 second try