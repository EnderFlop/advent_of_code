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
    memory_address = re.findall(r"[[]\d+[]]", x)[0][1:-1] #Gets (19747) out of mem[19747] = 52273994
    digit = int(x.split()[2]) #Gets (52273994) out of mem[19747] = 52273994
    binary = bin(digit).replace("0b", "") #turns digit into binary
    binary = binary.zfill(36) #adds leading zeros
    for index in range(len(mask)): #For each index in mask
      if mask[index] == "0": #If its a 0
        binary = binary[:index] + "0" + binary[index+1:] #change binary to be a 0 at that index
      elif mask[index] == "1": #If its a 1
        binary = binary[:index] + "1" + binary[index+1:] #change binary to be a 1 at that index
    decimal = int(binary, 2) #Change it back to decimal
    memory[memory_address] = decimal #At the memory_address, place that decimal
    
print(sum(memory.values()))

#PART 1 = 14954914379452