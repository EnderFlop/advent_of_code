import re
import itertools
import numpy as np
import time

#signal = open("2022/day6testinput.txt").read()
signal = open("2022/day6input.txt").read()

def detect_start(signal):
  for i in range(len(signal)):
    packet = signal[i:i+4]
    if len(set(packet)) == 4:
      return i + 4

print(detect_start(signal))
#part1 1100 first try! can't believe wrapping a string in set() does exactly what i wanted it to, isolate the letters and remove duplicates!