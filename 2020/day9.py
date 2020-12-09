import re

with open("2020/day9.txt") as text_file:
  text = text_file.read()

input = text.split("\n")
for i in range(len(input)):
  input[i] = int(input[i])
preamble = input[:25]
input = input[25:]

def test(number):
  for int_1 in preamble:
    for int_2 in preamble:
      #print(f"testing for {number}, {int_1} + {int_2} ({int_1 + int_2})")
      if int_1 + int_2 == number and int_1 != int_2:
        preamble.pop(0)
        preamble.append(number)
        return True
  return False

for number in input:
  if not test(number):
    print(number)
    break
  
