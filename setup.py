import requests
import os

YEAR = "2025"

try:
  os.chdir(os.getcwd() + f"\{YEAR}")
  print(f"\nCWD: {os.getcwd()}")
except FileNotFoundError:
  print("WARNING!!!")
  print("Directory not found!")
  print(f"CWD: {os.getcwd()}")
except NotADirectoryError:
  print("WARNING!!!")
  print("That's not a directory!")
  print(f"CWD: {os.getcwd()}")


DAY = input("What day would you like to start? ")
WRITES = f"import re\nimport itertools\nimport numpy as np\nimport time\n\ninstructions = open(\"{YEAR}/day{DAY}testinput.txt\").read().splitlines()\n#instructions = open(\"{YEAR}/day{DAY}input.txt\").read().splitlines()"

try:
  with open(f"day{DAY}.py", "x") as dayfile:
    dayfile.write(WRITES)
except FileExistsError:
  print(f"day{DAY} already exists!")

try:
  with open(f"day{DAY}testinput.txt", "x") as inputfile:
    pass
except FileExistsError:
  print(f"day{DAY} already exists!")

try:
  with open(f"day{DAY}input.txt", "x") as inputfile:
    pass
except FileExistsError:
  print(f"day{DAY} already exists!")