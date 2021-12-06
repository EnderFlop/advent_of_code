import re
import itertools
import numpy as np
import time

#instructions = open("2021/day6testinput.txt").read().split(",")
instructions = open("2021/day6input.txt").read().split(",")

lanternfish = [int(i) for i in instructions]
#the iterative approach will not work. much too long.

#a way to count multiple fish objects as one? all {day} fish as one object with a count of how many there are. 
# they can all count down together. only ever be 9 max objects

class FishChunk():
  def __init__(self, days):
    self.days = days
    self.count = 0
    self.breeding_fish = 0
  
  def __add__(self, value):
    self.count += value
  
  def __repr__(self):
    return f"{self.days}:{self.count}"
  
  def tick(self):
    if self.days == 0:
      #if it is the last day before breeding, when they tick "reset" all the fish (set them to 6 days) and "breed" new fish (8 days)
      self.breeding_fish = self.count
    else:
      fish_list[self.days - 1].__add__(self.count)
    self.count = 0

#set up with input
fish_list = [FishChunk(i) for i in range(9)]
for fish in lanternfish:
  fish_list[fish].__add__(1)

print(fish_list)
#run through days
for i in range(256):
  breeding_fish = 0
  for fish_chunk in fish_list:
    fish_chunk.tick()
  #it was ticking day 0 before ticking day 6 and day 8. I couldn't find a readable way to reverse the list without destroying index math.
  #this is slightly hacky (introducing a class variable only used by one instance) but it works for now.
  breeding_fish = fish_list[0].breeding_fish
  fish_list[8].__add__(breeding_fish)
  fish_list[6].__add__(breeding_fish)

print(sum([group.count for group in fish_list]))
#362740 part 1 first try! my optimization effort worked!
#1644874076764 part2! they just wanted me to run it on more days lol. destroyed it!