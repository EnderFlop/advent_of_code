import numpy as np

input = open("2016/day2.txt").read().splitlines()

keypad = np.array([[1,2,3],[4,5,6],[7,8,9]])
keypad_x = 1
keypad_y = 1
buttons = []
for i in input:
  for letter in i:
    print(letter)
    if letter == "L" and keypad_x != 0:
      keypad_x -= 1
    elif letter == "R" and keypad_x != 2:
      keypad_x += 1
    elif letter == "U" and keypad_y != 0: 
      keypad_y -= 1
    elif letter == "D" and keypad_y != 2:
      keypad_y += 1
  buttons.append(keypad[keypad_y][keypad_x])

print(buttons)
#part one 98575 first try