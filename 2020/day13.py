import re
import itertools
from functools import reduce
from rich.traceback import install
from rich.console import Console
install()
console = Console()

directions = open("2020/day13.txt").read().splitlines()
bus_ids = directions[1]
bus_ids = bus_ids.split(",")
ids_dict = {}
for i in range(len(bus_ids)):
  if bus_ids[i] != "x":
    ids_dict[int(bus_ids[i])] = int(bus_ids[i])-i

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

ids = list(ids_dict.keys())
remainders = list(ids_dict.values())
print(ids, remainders)
print(chinese_remainder(ids, remainders))
#751731698158528 is too low

#earliest time is 1000434, you could hop on 397 at 1000440, 6 after earliest PART1 = 2382
#PART2 = 906332393333683 thank u chinese remainder theorem