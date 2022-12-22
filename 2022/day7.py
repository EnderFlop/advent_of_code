import re
import itertools
import numpy as np
import time

#instructions = open("2022/day7testinput.txt").read().splitlines()
instructions = open("2022/day7input.txt").read().splitlines()

class Directory():
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.subdirectories = {}
    self.files = []
  
  def set_parent(self, directory):
    self.parent = directory
  
  def add_subdirectory(self, directory):
    dir = Directory(directory)
    dir.set_parent(self)
    self.subdirectories[directory] = dir
  
  def add_file(self, file):
    self.files.append(file)

def build_filesystem(current_directory):
  for i in instructions:

    if i[0] != "$": #if NOT a command, add files and dirs until done
      splt = i.split(" ")
      if splt[0] == "dir":
        current_directory.add_subdirectory(splt[1])
      else:
        current_directory.add_file(int(splt[0]))
    
    else:
      splt = i.split(" ")
      if splt[1] == "ls":
        continue
      if splt[2] == "..":
        current_directory = current_directory.parent
      else:
        current_directory = current_directory.subdirectories[splt[2]]
    
    #print(current_directory.name, current_directory.files, current_directory.subdirectories)

sizes = []

def iterate_filesystem(current_dir):
  global sizes
  size = sum(current_dir.files)
  for sub_dir in current_dir.subdirectories.values():
    size += iterate_filesystem(sub_dir)
  print(current_dir.name, size)

  sizes.append(size)
  
  return size

parent_dir = Directory("/")
build_filesystem(parent_dir)
iterate_filesystem(parent_dir)

all_files_size = max(sizes) #size of "/" dir, all files
space_remaining = 70000000 - all_files_size #constant 70 million disk space
space_needed = 30000000 - space_remaining
new_sizes = [s for s in sizes if s >= space_needed]
print(min(new_sizes))

#part1 46952861 too high, 1908462 second try. accidentally stuck an extra 0 in the size test, whoops
#part2 3979145 first try!