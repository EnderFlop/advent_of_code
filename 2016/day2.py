import numpy as np

input = open("2016/day2.txt").read().splitlines()

keypad = np.array([["x", "x", 1, "x", "x"],["x", 2,3,4, "x"],[5,6,7,8,9],["x", "A","B","C", "x"],["x", "x", "D", "x", "x"]])
keypad_x = 0
keypad_y = 2
buttons = []
print(keypad[keypad_y][keypad_x])

for i in input:
  for letter in i:
    print(letter)
    if letter == "L" and keypad_x != 0 and keypad[keypad_y][keypad_x - 1] != "x":
      keypad_x -= 1
    elif letter == "R" and keypad_x != 4 and keypad[keypad_y][keypad_x + 1] != "x":
      keypad_x += 1
    elif letter == "U" and keypad_y != 0 and keypad[keypad_y - 1][keypad_x] != "x":
      keypad_y -= 1
    elif letter == "D" and keypad_y != 4 and keypad[keypad_y + 1][keypad_x] != "x":
      keypad_y += 1
  print(keypad[keypad_y][keypad_x])
  buttons.append(keypad[keypad_y][keypad_x])

print(buttons)
#part one 98575 first try
#part two CD8D4 first try
#this is some shitty code, but I don't know enough about numpy to put an array at a specific point on top of another array without just using junk to place it there
#I don't think there is any, that's why numpy can fill your array with periods or zeros.
#There's still a better way to check, but this works for my use case. 