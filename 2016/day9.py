import re
import itertools
import numpy as np
import time
import string

compressed = open("2016/day9.txt").read()

#def decompress(compressed):
  #for each index, character:
    #if the index is within the already seen range:
      #ignore
    #elif it is a regular character:
      #length += 1
    #elif it is an opening parenthasis:
      #get the marker
      #find the region it holds
      #find all the markers inside that region
      #find the markers they hold, continue. (recursive?)
      #break when no more markers in a given region. return the length of that region multiplied by the count of the marker it was inside.
      #length += returned value
  #return length

def go_inside(region, count):
  if "(" not in region:
    return count * len(region)
  return count * decompress(region)

def decompress(compressed):
  total_length = 0
  start_index = -1
  end_index = -1
  region_size = -1
  for index, character in enumerate(compressed):
    #print(start_index, end_index, region_size)
    if index in range(start_index, end_index + region_size + 1):
      pass
    elif character == "(":
      start_index = index
    elif character == ")":
      end_index = index
      marker = compressed[start_index+1:end_index]
      region_size, count = int(marker.split("x")[0]), int(marker.split("x")[1])
      string_region = compressed[end_index + 1:end_index + region_size + 1]
      total_length += go_inside(string_region, count)
    elif character in string.ascii_uppercase:
      total_length += 1
  return total_length

print(decompress(compressed))

#120765 first try! index math is hard for me, super glad I managed to figure this one out!

#PART 2 Planning:
# We can't use the traditional scan and decompress method, there must be math involved.
# (27x12)(20x12)(13x14)(7x10)(1x12)A
# read (27x12): multiply the next 27 characters 12 times
# 12 * (20x12)(13x14)(7x10)(1x12)A
# read (20x12): multiply the next 20 characters 12 times
# etc. 12*12*14*10*12*1 = 241920. Correct answer.
# For everything inside a region, the total length will be the inside counts multiplied together.

#11658395076 !!!!!! FIRST TRY !!!!! WITH A WIERD DOUBLE RECURSIVE FUNCTION AND SUDOCODE !!!!!
# I'M FREAKING OUT RIGHT NOW LETS GET IT! It's like the golden bag problem all over again!
