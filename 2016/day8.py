import re
import itertools
import numpy as np
import time

instructions = open("2016/day8.txt").read().splitlines()

array_x = 50
array_y = 6
lcd = np.full((array_y,array_x), ".")

for transform in instructions:
  command = transform.split()[0]
  if command == "rect":
    coords = transform.split()[1].split("x")
    x_wide = int(coords[0])
    y_tall = int(coords[1])
    for x in range(x_wide):
      for y in range(y_tall):
        lcd[y][x] = "#"
  
  elif command == "rotate":
    row_or_column = transform.split()[1]
    if row_or_column == "row":
      row_index = int(transform.split()[2].split("=")[1])
      shift_factor = int(transform.split()[4])
      lcd[row_index,:] = np.roll(lcd[row_index,:], shift_factor)
    elif row_or_column == "column":
      column_index = int(transform.split()[2].split("=")[1])
      shift_factor = int(transform.split()[4])
      lcd[:,column_index] = np.roll(lcd[:,column_index], shift_factor)

#part1 119 first try! even identified a bug before it became a problem, with integers being longer than one character. Extracting information from english commands sucks

#print the first five columns . print a new line.
#lcd = np.rot90(lcd)
#lcd = np.rot90(lcd)
#lcd = np.rot90(lcd)
#print(lcd)

#part2 ZFHFSFOGPO! just had to rotate the array a few times and turn my head. Definetly not the best way to do it, put a more creative one I guess
#I experimented with printing out certain columns but then the display was still sideways. Maybe if I had rotated the individual columns before I printed them?
#Maybe a test for another time, I have to go put up a christmas tree
lcd = np.split(lcd, 10, axis=1)
for letter in lcd:
  print(letter)
  print("\n")
#went back and made a cleaner way of doing it. learned how to use np.split too!