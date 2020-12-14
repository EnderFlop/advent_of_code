import re
import itertools
from rich.traceback import install
from rich.console import Console
install()
console = Console()

text = open("2020/day12.txt").read().splitlines()
console.log(text)
console.log("hello!")
def test_func(asd, dsf):
  print(asd/dsf)

test_func(3, 0)