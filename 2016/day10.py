import re
import itertools
import numpy as np
import time
import random

instructions = open("2016/day10.txt").read().splitlines()

class Output():
  def __init__(self, id):
    self.id = id
    self.value = None

  def receive_value(self, value):
    self.value = value
  
  def get_id(self):
    return self.get_id

class Bot():
  def __init__(self, id, low=None, high=None):
    self.id = id
    self.low = low
    self.high = high
    self.command = ""
  
  def receive_value(self, value):
    high = self.get_high()
    low = self.get_low()

    #If both values are populated (will never happen)
    if low is not None and high is not None:
      print("Collision!")
    #If neither value is populated, shove value in bot
    if low is None and high is None:
      self.set_high(value)
    #If high is populated and low is not
    if high is not None and low is None:
      #if value is bigger than high, move values
      if value > high:
        self.set_low(high)
        self.set_high(value)
      #if value is lower, place in low
      if value < high:
        self.set_low(value)
    #If low is populated and high is not
    if high is None and low is not None:
      #if value is smaller than low, move values
      if value < low:
        self.set_high(low)
        self.set_low(value)
      #if value is bigger, place in high
      if value > low:
        self.set_high(value)
  
  def give_value(self, low_or_high, reciever):
    if low_or_high == "low":
      reciever.receive_value(self.get_low())
      self.set_low(None)
    if low_or_high == "high":
      reciever.receive_value(self.get_high())
      self.set_high(None)
  
  def has_both_microchips(self):
    return self.get_low() and self.get_high()
  
  def set_high(self, value):
    self.high = value
  
  def set_low(self, value):
    self.low = value
  
  def get_high(self):
    return self.high
  
  def get_low(self):
    return self.low
  
  def get_id(self):
    return self.id
  
  def set_command(self, command):
    self.command = command
  
  def get_command(self):
    return self.command

  def execute_command(self):
    words = self.get_command().split()
    first_machine = words[-7]
    first_id = int(words[-6])
    second_machine = words[-2]
    second_id = int(words[-1])
    #give low value
    if first_machine == "bot":
      self.give_value("low", bots_list[first_id])
    elif first_machine == "output":
      self.give_value("low", output_list[first_id])
    #Give high value
    if second_machine == "bot":
      self.give_value("high", bots_list[second_id])
    elif second_machine == "output":
      self.give_value("high", output_list[second_id])

  def check_answer(self):
    if self.get_low() == 17 and self.get_high() == 61:
      return True
    return False

#initializing bots and outputs
bots_list = {}
output_list = {}
for i in range(250):
  bots_list[i] = Bot(id=i)
for i in range(50):
  output_list[i] = Output(id=i)

#initalizing bots
for command in instructions:
  words = command.split()
  if words[0] == "value":
    value = int(words[1])
    bot_number = int(words[-1])
    bots_list[bot_number].receive_value(value)

  if words[0] == "bot":
    giving_bot_id = int(words[1])
    giving_bot = bots_list[giving_bot_id]
    giving_bot.set_command(command)


valid_bots = [bot for bot in bots_list.values() if bot.has_both_microchips()]
while valid_bots:
  #print([f"bot{k}: {v.get_low()}, {v.get_high()}" for k,v in bots_list.items()])
  valid_bots = [bot for bot in bots_list.values() if bot.has_both_microchips()]
  random.shuffle(valid_bots)
  #print([bot.id for bot in valid_bots])
  for bot in valid_bots:
    if bot.get_low() == 17 or bot.get_high() == 17:
      print(f"{bot.id} currently has 17")
    if bot.get_low() == 61 or bot.get_high() == 61:
      print(f"{bot.id} currently has 61")
    if bot.check_answer():
      print(f"WE FOUND IT! BOT {bot.id}. MICROCHIPS {bot.get_low()} & {bot.get_high()}")
    bot.execute_command()

#first try bot 119. too high.
#Maybe run the bot's program the second that it gets two microchips instead of waiting around? Tried that, ran into no answer (even without the random shuffle).
# 118 is also too high. Just seeing if the bots weren't zero indexed or something stupid lol
#73, part1, needed some reddit help! my receive value function was off, low and high were getting unordered. reworked it with descriptive comments, works great.