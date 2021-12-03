import re
import itertools
import numpy as np
import time

instructions = open("2021/day3.txt").read().splitlines()

def decimalToBinary(n):
    return bin(n).replace("0b","")

def binaryToDecimal(n):
    return int(n,2)

grid = [[i for i in x] for x in instructions] #double list comprehension!
grid = np.asarray(grid)

#valid_list = all rows in grid
#for every column index.
  #for every row in the valid_list.
    #Scan the column index bit of every row and see which one is larger.
    #Add the row to a "ones_list" or a "zeroes_list"
  #If there are more ones, or equal zeroes and ones
    #continue onto the next column with valid_list = "ones_list"
  #if there are more zeros
    #continue onto the next column with valid_list = "zeroes_list"
  

valid_rows = [list(grid[i]) for i in range(len(grid))]
for column_index in range(len(grid[0])):
  zero_count = 0
  one_count = 0
  zeroes_list = []
  ones_list = []
  if len(valid_rows) == 1:
    break
  for row in valid_rows:
    current_bit = row[column_index]
    if current_bit == "0":
      zero_count += 1
      zeroes_list.append(row)
    elif current_bit == "1":
      one_count += 1
      ones_list.append(row)
  if one_count < zero_count:
    valid_rows = ones_list
  elif zero_count <= one_count:
    valid_rows = zeroes_list

co2_str = "".join(valid_rows[0])
co2_rating = binaryToDecimal(co2_str)
print(co2_rating)

#OXYGEN_RATING = 3089
#CO2_RATING = 257
print(3089 * 257)

#part1 3827 too low. Just realized I didnt even read the second half of the puzzle. Should be pretty easy from here.
#part1 1025636. Just had to actually finish the problem.
#part2 793873. first try! feels ugly that I had to change the program to get the two different values, but all I did was change the greater thans etc.