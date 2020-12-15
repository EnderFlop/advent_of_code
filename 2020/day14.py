import re
import itertools
from rich.traceback import install
from rich.console import Console
install()
console = Console()

asdf = open("2020/day14.txt").read().splitlines()
memory = {}
mask = "0"


for x in asdf:
  command = re.match(r"\b\w+\b", x).group(0)
  if command == "mask":
    mask = x.split()[2]
  else:
    x_indexes = [] #List of all indecies that have an x
    memory_address = re.findall(r"[[]\d+[]]", x)[0][1:-1] #Gets (19747) out of mem[19747] = 52273994
    digit = int(x.split()[2]) #Gets (52273994) out of mem[19747] = 52273994
    binary = bin(int(memory_address)).replace("0b", "") #turns memory address into binary
    binary = binary.zfill(36) #adds leading zeros
    for index in range(len(mask)): #For each index in mask
      if mask[index] == "0": #If its a 0
        pass
      elif mask[index] == "1": #If its a 1
        binary = binary[:index] + "1" + binary[index+1:] #change binary to be a 1 at that index
      elif mask[index] == "X":
        binary = binary[:index] + "X" + binary[index+1:] #change binary to be a X at that index
        x_indexes.append(index)
    perms = itertools.product("01", repeat=len(x_indexes)) #Get all the cartesian product of 0 and 1 with a length of the amount of x's in the adress
    for i in perms: #For each permutation
      new_binary = binary #Placeholder
      for x in range(len(x_indexes)): #For each x index in x_indexes
        new_binary = new_binary[:x_indexes[x]] + i[x] + new_binary[x_indexes[x]+1:] #Change the index from an X to whatever index of the permutation we are on (i = i[:x_indexes[0]] + i[0] + i[x_indexes[0]+1:])
      decimal = int(new_binary, 2) #Change it back to decimal
      memory[decimal] = digit #Set that memory address to the original value
    
print(sum(memory.values()))

#PART 1 = 14954914379452
#PART 2 = 3869978490834256 TOO HIGH
#PART 2 = 3415488160714 FIXED IT