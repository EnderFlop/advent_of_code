import re
import itertools
from rich.traceback import install
from rich.console import Console
install()
console = Console()

directions = open("2020/day12.txt").read().splitlines()

class Ship():
  def __init__(self):
    self.degrees_direction = 90 #In degrees. 0 = North, 90 = East, 180 = South, 270 = West
    self.cardinal_direction = "E"
    self.direction_dict = {
      0: "N",
      90: "E",
      180: "S",
      270: "W"
    }
    self.vertical_position = 0
    self.horizontal_position = 0

  def run_command(self, command, units):
    console.log(f"RUNNING COMMAND {command} WITH UNITS {units}")
    if command in ["F", "N", "E", "S", "W"]:
      self.move(command, units)
    elif command in ["R", "L"]:
      self.rotate(command, units)
    else:
      raise NameError(f"Unknown command issued to ship! COMMAND:{command} UNITS:{units}")

  def change_cardinal(self):
    self.cardinal_direction = self.direction_dict[self.degrees_direction % 360] #Mod 360 to keep it in a circle scale

  def move(self, direction, units): 
    #If F, move in self.direction x units
    #If anything else, move in that direction by that many units
    if direction == "F": #Changes direction to the current direction the ship is facing
      direction = self.cardinal_direction
    
    #VERTICAL ADJUSTERS
    if direction == "N":
      self.vertical_position += units
    elif direction == "S":
      self.vertical_position -= units
    #HORIZONTAL ADJUSTERS
    elif direction == "E":
      self.horizontal_position += units
    elif direction == "W":
      self.horizontal_position -= units

  def rotate(self, direction, degrees):
    #If right, positive. Left, negative.
    if direction == "R":
      self.degrees_direction += degrees
      self.change_cardinal()
    elif direction == "L":
      self.degrees_direction -= degrees
      self.change_cardinal()

ship = Ship()

for i in directions:
  command = i[0]
  units = int(i[1:])
  ship.run_command(command, units)

print(abs(ship.vertical_position) + abs(ship.horizontal_position))
#NOT 4789, too high
#415! The degree direction was going way past 360 and it was tripping up the change_cardinal method