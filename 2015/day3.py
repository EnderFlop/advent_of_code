with open("2015/day3.txt") as text_file:
  instructions = text_file.read()

matrix = {
  (0,0) : 2
}

def make_move(player, direction):
  if direction == "^":
    player[1] += 1 #Increase Y by 1
  elif direction == "v":
    player[1] -= 1 #Decrease Y by 1
  elif direction == ">":
    player[0] += 1 #Increase X by 1
  elif direction == "<":
    player[0] -= 1 #Decrease X by 1

santa_pos = [0,0]
robo_pos = [0,0]
santa_turn = True
for move in instructions:
  if santa_turn == True:
    make_move(santa_pos, move)
    key = tuple(santa_pos)
  else:
    make_move(robo_pos, move)
    key = tuple(robo_pos)
  if key in matrix:
    matrix[key] += 1
  else:
    matrix[key] = 1
  santa_turn = not santa_turn
  print(santa_pos, robo_pos)

print(len(matrix))

