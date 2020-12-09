import re

with open("2020/day8.txt") as text_file:
  text = text_file.read()

instructions = text.split("\n")

visited = {}
for index in range(len(instructions)):
  visited[index] = False
print(visited)

def run_action(index):
  command, argument = instructions[index].split(" ")[0], int(instructions[index].split(" ")[1])
  if visited[index] == True:
    return 0
  visited[index] = True
  if command == "nop":
    return run_action(index+1)
  elif command == "jmp":
    return run_action(index + argument)
  elif command == "acc":
    return argument + run_action(index+1)

print(run_action(0))