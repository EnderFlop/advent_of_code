

with open("2015/day8.txt") as text_file:
  text = text_file.read()

text = text.split("\n")

len_raw_string = 0
len_encode_string = 0

for string in text:
  len_raw_string += len(string)
  print(string)
  string = string.replace("\\", "\\\\")
  string = string.replace("\"", "\\\"")
  string = "\"" + string + "\""
  print(string)
  len_encode_string += len(string)

print(len_encode_string - len_raw_string)