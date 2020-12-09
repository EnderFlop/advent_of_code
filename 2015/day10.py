from itertools import groupby

input = "3113322113"
#real input = "3113322113"


def look_and_say(number, loop_count):
  for i in range(loop_count):
    return_string = ""
    print(f"loop #{i}")
    for k, g in groupby(number):
      return_string += str(len(list(g))) + str(k)
    number = return_string
  return number

print(f"after 50 runs, input is {len(look_and_say(input, 50))} long")
  