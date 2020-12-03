with open("2015/day5.txt") as text_file:
  strings = text_file.read()

def pair_check(string):
  for index in range(len(string) - 1):
    check_letters = string[index : index+2]
    if check_letters in string.replace(check_letters, " ", 1):
      print(f"{string} contains {check_letters} twice")
      return True

def x_y_x(string):
  for index in range(len(string) - 2):
    if string[index] == string[index + 2]:
      #print(f"Index {index} ({string[index]}) and index {index + 2} ({string[index + 2]}) are identical")
      return True
  return False

strings = strings.split("\n")
nice_strings = 0
for string in strings:
  if pair_check(string):
    if x_y_x(string):
      #print(f"{string} passes all tests.")
      nice_strings += 1
print(nice_strings)
