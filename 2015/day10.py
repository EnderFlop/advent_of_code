input = "3113322113"
#real input = "3113322113"

def look_and_say(number, count):
  #print(f"\nnumber = {number}, count = {count}")  
  if count == 40:
    return number
  list = []
  #Get lengths of numbers in a row
  index = 0
  row_length = 0
  while number:
    row_length += 1
    #print(f"number = {number}. index = {index}. number[index] = {number[index]}")
    try:
      if number[index] == number[index + 1]:
        index += 1
      else:
        append_string = str(row_length) + str(number[index])
        list.append(append_string)
        number = number[index+1:]
        row_length = 0
        index = 0
    except IndexError:
      list.append(str(row_length) + str(number[index]))
      number = None
      
  s = [str(i) for i in list] 
  res = "".join(s)
  count += 1
  return(look_and_say(res, count))

number = look_and_say(input, 0)
print(len(number))
  