import re
import itertools
import numpy as np
import time
import string

compressed = open("2016/day9.txt").read()

def decompress(compressed):
  decompressed = ""
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
      decompressed += string_region * count
    elif character in string.ascii_uppercase:
      decompressed += character
  return decompressed

result = decompress(compressed)
#print(result)
print(f"len = {len(result)}")
#120765 first try! index math is hard for me, super glad I managed to figure this one out!