import re
import itertools
from rich.traceback import install
from rich.console import Console
install()
console = Console()

directions = open("2020/day12.txt").read().splitlines()

class Waypoint_And_Ship():
  def __init__(self):
    self.waypoint_vert = 1
    self.waypoint_hori = 10
    self.ship_vert = 0
    self.ship_hori = 0

  def run_command(self, command, units):
    console.log(f"RUNNING COMMAND {command} WITH UNITS {units}")
    if command in ["N", "E", "S", "W"]:
      self.move_waypoint(command, units)
    elif command in ["R", "L"]:
      self.rotate_waypoint(command, units)
    elif command in ["F"]:
      self.move_ship(units)
    else:
      raise NameError(f"Unknown command issued to ship! COMMAND:{command} UNITS:{units}")

  def move_ship(self, moves):
    #MOVE SHIP TOWARDS WAYPOINT {moves} AMOUNT OF TIMES
    #ship coords += waypoint coords x times?
    self.ship_hori += self.waypoint_hori * moves
    self.ship_vert += self.waypoint_vert * moves

  def move_waypoint(self, direction, units): 
    #VERTICAL ADJUSTERS
    if direction == "N":
      self.waypoint_vert += units
    elif direction == "S":
      self.waypoint_vert -= units
    #HORIZONTAL ADJUSTERS
    elif direction == "E":
      self.waypoint_hori += units
    elif direction == "W":
      self.waypoint_hori -= units

  def rotate_waypoint(self, direction, degrees):
    #https://calcworkshop.com/wp-content/uploads/common-rotations-origin.png
    if direction == "R": #CLOCKWISE
      if degrees == 90:
        self.waypoint_hori, self.waypoint_vert = self.waypoint_vert, (-1*self.waypoint_hori) #(x,y) -> (y,-x)
      elif degrees == 180:
        self.waypoint_hori, self.waypoint_vert = (-1*self.waypoint_hori), (-1*self.waypoint_vert) #(x,y) -> (-x,-y)
      elif degrees == 270:
        self.waypoint_hori, self.waypoint_vert = (-1*self.waypoint_vert), self.waypoint_hori #(x,y) -> (-y, x)

    elif direction == "L": #COUNTERCLOCKWISE
      if degrees == 90:
        self.waypoint_hori, self.waypoint_vert = (-1*self.waypoint_vert), self.waypoint_hori #(x,y) -> (-y, x)
      elif degrees == 180:
        self.waypoint_hori, self.waypoint_vert = (-1*self.waypoint_hori), (-1*self.waypoint_vert) #(x,y) -> (-x,-y)
      elif degrees == 270:
        self.waypoint_hori, self.waypoint_vert = self.waypoint_vert, (-1*self.waypoint_hori) #(x,y) -> (y,-x)


ship = Waypoint_And_Ship()

for i in directions:
  command = i[0]
  units = int(i[1:])
  ship.run_command(command, units)

print(abs(ship.ship_hori) + abs(ship.ship_vert))
#NOT 4789, too high
#415! The degree direction was going way past 360 and it was tripping up the change_cardinal method

#PART 2 29401 FIRST TRY!!!!!