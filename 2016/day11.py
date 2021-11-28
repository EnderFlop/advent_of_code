import re
import itertools
import numpy as np
import time

instructions = open("2016/day11.txt").read().splitlines()

class Floor():
  def __init__(self, number, microchips = None, generators = None):
    self.number = number
    self.microchips = microchips
    self.generators = generators

class Generator():
  def __init__(self, element):
    self.element = element
    self.microchip = None
  
  def insert_microchip(microchip):
    if self.element == microchip.element:
      print(f"microchip {element} inserted into generator {self.element}")
      self.microchip = microchip
    else:
      print("element collision!")
  
  def remove_microchip(self):
    pass


#While all generators and microchips arent on floor one
  #If nothing is in the elevator
    #pick up to two items (have to figure out logic here)
  #if something is in elevator
    #if there 

#11/27/2021 I have no idea how to even begin making this the most efficient. I don't even know how to get started. 
#If I tried for hours I could probably get a working, inefficient simulation going, then in a few more hours I could improve it. I don't have the drive right now