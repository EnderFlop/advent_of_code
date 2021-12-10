import re
import itertools
import numpy as np
import time

#instructions = open("2021/day10testinput.txt").read().splitlines()
instructions = open("2021/day10input.txt").read().splitlines()

front_to_back = {"(": ")", "{": "}", "[": "]", "<": ">"}
back_to_front = {v:k for k,v in front_to_back.items()}
points_lookup = {")":1, "]":2, "}":3, ">":4}

class Stack():
  def __init__(self):
    self.stack = []
  
  def __repr__(self):
    return str(self.stack)
  
  def put(self, value):
    self.stack.insert(0, value)
  
  def get(self):
    value = self.stack[0]
    self.stack = self.stack[1:]
    return value
  
  def peek_top(self):
    return self.stack[0]
  
  def length(self):
    return len(self.stack)
  

def go_inside(chunk):
  if len(chunk) == 0:
    return True
  if chunk[0] in ["(", "[", "{", "<"]: #if it is a starting character
    bracket_stack.put(chunk[0]) #add that to the queue
    return go_inside(chunk[1:]) #continue down the chunk
  #if it is an ending character and there are no starting characters to match to
  if chunk[0] in [")", "]", "}", ">"] and bracket_stack.length() == 0:
    return chunk[0] #return the corrupted char 
  #if it is an ending character and not the finisher to the most recent starting character
  if chunk[0] in [")", "]", "}", ">"] and bracket_stack.peek_top() != back_to_front[chunk[0]]:
    return chunk[0] #return the corrupted char
  #if it is an ending character but it finishes a starting character
  if chunk[0] in [")", "]", "}", ">"] and bracket_stack.peek_top() == back_to_front[chunk[0]]:
    bracket_stack.get() #remove the starting char
    return go_inside(chunk[1:]) #continue down the chunk
    
points_list = []
for i in instructions:
  bracket_stack = Stack()
  point_total = 0
  result = go_inside(i)
  if result == True:
    while bracket_stack.length() != 0:
      bracket_to_finish = bracket_stack.get()
      finisher = front_to_back[bracket_to_finish]
      point_total *= 5
      point_total += points_lookup[finisher]
    points_list.append(point_total)

points_list.sort()
print(points_list[len(points_list) // 2])
#271245 part1 first try! had to impliment my own stack that let me peek at the top number without returning it, but it works!
#1685293086 part2 first try! a lot faster than previous days. feeling good.