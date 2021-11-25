import re
import itertools
import numpy as np
import time
import hashlib

start = time.time()
instructions = open("2016/day5.txt").read()

password = ["!", "!", "!", "!", "!", "!", "!", "!"] #eight placeholder dead characters
i = 0
while "!" in password:
  to_be_hashed = instructions + str(i)
  hash = hashlib.md5(to_be_hashed.encode("utf-8"))
  hex = hash.hexdigest()
  if hex[0:5] == "00000":
    index = hex[5]
    character = hex[6]
    if index.isnumeric() and int(index) <= 7 and password[int(index)] == "!":
      password[int(index)] = character
      print(password)
  i += 1

end = time.time()
print(end - start)

print("".join(password).strip())

#part1 801b56a7 first try! took around 9 seconds. I wonder if theres a faster way than brute force. 
# I imagine this would take a very long time if it asked to find six leading zeroes
#part2 424a0197 first try! this took 30.8 seconds.