import re

with open("2020/day8.txt") as text_file:
  text = text_file.read()

instructions = text.split("\n")

def reset_visited():
  visited = {}
  for index in range(len(instructions)):
    visited[index] = False
  return visited

def run_action(index):
  try:
    command, argument = instructions[index].split(" ")[0], int(instructions[index].split(" ")[1])
  except IndexError:
    if index == 601:
      return True
    else:
      return False
  if visited[index] == True:
    print(f"already visited {index}, returning false")
    return False
  visited[index] = True
  if command == "acc": 
    return run_action(index + 1)
  if command == "nop":
    return run_action(index + 1)
  if command == "jmp":
    return run_action(index + argument)

def accumulate(index):
  try:
    command, argument = instructions[index].split(" ")[0], int(instructions[index].split(" ")[1])
  except IndexError:
    if index == 601:
      return 0
  if visited[index] == True:
    return 0
  visited[index] = True
  if command == "nop":
    return accumulate(index+1)
  elif command == "jmp":
    return accumulate(index + argument)
  elif command == "acc":
    return argument + accumulate(index+1)

for index in range(len(instructions)):
  visited = reset_visited()
  command, argument = instructions[index].split(" ")[0], instructions[index].split(" ")[1]
  if command == "nop":
    print(f"instructions[{index}] is 'nop', changing to 'jmp'.")
    instructions[index] = "jmp " + argument
  if command == "jmp":
    print(f"instructions[{index}] is 'jmp', changing to 'nop'.")
    instructions[index] = "nop " + argument
  if run_action(0):
    print(index)
    break
  else:
    command, argument = instructions[index].split(" ")[0], instructions[index].split(" ")[1]
    if command == "nop":
      print(f"not successful, changing back 'nop' back to 'jmp'.")
      instructions[index] = "jmp " + argument
    if command == "jmp":
      print(f"not successful, changing back 'jmp' back to 'nop'.")
      instructions[index] = "nop " + argument

visited = reset_visited()
print(accumulate(0))
#Index 19 needs to be turned from jmp to nop