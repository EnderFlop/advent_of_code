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
gamma_bit_list = []
epsilon_bit_list = []
for column in range(len(grid[0])):
  zero_count = 0
  one_count = 0
  for unit in grid[:,column]:
    if unit == "0":
      zero_count += 1
    elif unit == "1":
      one_count += 1
  if zero_count > one_count:
    gamma_bit_list.append(0)
    epsilon_bit_list.append(1)
  elif one_count > zero_count:
    gamma_bit_list.append(1)
    epsilon_bit_list.append(0)

gamma_str = "".join([str(i) for i in gamma_bit_list])
epsilon_str = "".join([str(i) for i in epsilon_bit_list])
print(f"Gamma: {binaryToDecimal(gamma_str)}. Epsilon: {binaryToDecimal(epsilon_str)}")
print(f"Multiplied: {binaryToDecimal(gamma_str) * binaryToDecimal(epsilon_str)}")
#part1 3827 too low. Just realized I didnt even read the second half of the puzzle. Should be pretty easy from here.
#part1 1025636. Just had to actually finish the problem.