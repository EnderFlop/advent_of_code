with open("2015/day5.txt") as text_file:
  strings = text_file.read()

def count_vowels(string):
  vowels = 0
  vowels += string.count("a")
  vowels += string.count("e")
  vowels += string.count("i")
  vowels += string.count("o")
  vowels += string.count("u")
  return vowels

def double_letter(string):
  alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for letter in alphabet_list:
    if string.find(letter*2) != -1:
      return True
  return False

def forbidden_strings(string):
  forbidden_list = ["ab", "cd", "pq", "xy"]
  for forbidden in forbidden_list:
    if string.find(forbidden) != -1:
      return False
  return True

strings = strings.split("\n")
nice_strings = 0
for string in strings:
  if count_vowels(string) >= 3:
    if double_letter(string):
      if forbidden_strings(string):
        print(f"{string} passes all tests")
        nice_strings += 1
print(nice_strings)

