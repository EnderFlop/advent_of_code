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

  def recieve_value(self, value):
    self.value = value
  
  def get_id(self):
    return self.get_id

class Bot():
  def __init__(self, id, low=None, high=None):
    self.id = id
    self.low = low
    self.high = high
    self.command = ""
  
  def recieve_value(self, value):
    if self.get_high() == None:
      self.set_high(value)
    elif self.get_low() == None:
      self.set_low(value)
    elif value > self.get_high():
      self.set_low(self.get_high())
      self.set_high(value)
    elif value < self.get_low():
      self.set_high(self.get_low())
      self.set_low(value)
  
  def give_value(self, low_or_high, reciever):
    if low_or_high == "low":
      reciever.recieve_value(self.get_low())
      self.set_low(None)
    if low_or_high == "high":
      reciever.recieve_value(self.get_high())
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
    bots_list[bot_number].recieve_value(value)

  elif words[0] == "bot":
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