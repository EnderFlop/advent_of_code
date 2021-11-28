import re
import itertools
import numpy as np
import time

instructions = open("2016/day11.txt").read().splitlines()

class Floor():
  def __init__(self, floor_number, microchips = [], generators = []):
    self.floor_number = floor_number
    self.microchips = microchips
    self.generators = generators
  
  def load(self, thing):
    if type(thing) == Microchip:
      self.microchips += thing
    if type(thing) == Generator:
      self.generators += thing
  
  def unload(self, thing):
    if type(thing) == Microchip:
      self.microchips.remove(thing)
    if type(thing) == Generator:
      self.generators.remove(thing)
  
  def amount(self):
    return len(self.microchips) + len(self.generators)
  
  def danger_check(self):
    temp_chips = self.microchips.copy()
    temp_gens = self.generators.copy()
    okay_items = []
    for chip in temp_chips:
      for gen in temp_gens:
        if chip.get_element() == gen.get_element(): #If there is a matching pair, remove it
          print(f"Pair! {chip} {gen}")
          okay_items.append(chip)
          okay_items.append(gen)
    for item in okay_items:
      if type(item) == Generator:
        temp_gens.remove(item)
      else:
        temp_chips.remove(item)
    if len(temp_chips) >= 1 and len(temp_gens) >= 1:
      return True
    return False

class Elevator():
  def __init__(self, contents=[], floor=1):
    self.contents = contents
    self.floor = floor
  
  def load(self, thing):
    floors_list[self.floor + 1].unload(thing)
    self.contents += thing
  
  def unload(self, thing):
    floors_list[self.floor + 1].load(thing)
    self.contents.remove(thing)
  
  def danger_check(self): #Returns True if the items in the elevator interfere with eachother, False if there is no danger
    generator_list = []
    microchip_list = []
    for item in self.contents:
      if type(item) == Generator:
        generator_list += item
      elif type(item) == Microchip:
        microchip_list += item
    
    #If there is just one microchip and just one generator, they must be the same element
    #otherwise, two microchips and two generators are just fine
    if len(generator_list) == 1 and len(microchip_list) == 1:
      if generator_list[0].get_element() != microchip_list[0].get_element():
        print("Danger! Elevator contains competing items")
        return True
    return False
  
  def move_floor(self, up_or_down):
    if self.contents == []:
      print("elevator can't move! Needs something inside")
    elif len(self.contents) > 2:
      print("too many items in elevator!")
    if self.danger_check():
      print("can't move floors! Danger in elevator!")

    elif up_or_down == "up":
      self.floor += 1
    elif up_or_down == "down":
      self.floor -= 1

class Generator():
  def __init__(self, element):
    self.element = element
  
  def __repr__(self):
    return self.element + " "  + type(self).__name__
  
  def get_element(self):
    return self.element

class Microchip(Generator):
  pass

h_gen = Generator("Hydrogen")
h_mic = Microchip("Hydrogen")
l_gen = Generator("Lithium")
l_mic = Microchip("Lithium")

floors_list = [Floor(1, microchips=[h_mic, l_mic]),Floor(2, generators=[h_gen]),Floor(3, generators=[l_gen]),Floor(4)]

floor5 = Floor(5, generators=[Generator("A"), Generator("C"), Generator("B")], microchips=[Microchip("B"), Microchip("A"), Microchip("D")])
print(floor5.danger_check())


step_count = 0
#while floors_list[3].amount() != 4: (while floor four doesn't have every item) 
for i in range(5):
  pass

#RULES
#Generator and Microchip of two different elements cant be on same floor (or elevator ride) unless microchip is attached to it's generator
#Elevator can only carry two items, must carry at least one to move
#get everything to floor four


#While all generators and microchips arent on floor one
  #If nothing is in the elevator
    #pick up to two items (have to figure out logic here)
  #if something is in elevator
    #if there 
