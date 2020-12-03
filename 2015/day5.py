with open("2015/day5.txt") as text_file:
  strings = text_file.read()

def pair_check(string):
  for index in range(len(string) - 1):
    if string[index : index+2] in string.replace(string[index : index+2], " ", 1):
      return True

def x_y_x(string):
  for index in range(len(string) - 2):
    if string[index] == string[index + 2]:
      return True

strings = strings.split("\n")
nice_strings = 0
for string in strings:
  if pair_check(string) and x_y_x(string):
    nice_strings += 1
print(nice_strings)
