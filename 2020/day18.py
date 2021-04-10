import re
import itertools
import numpy as np
import time

instructions = open("2020/day18.txt").read().splitlines()
#instructions = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

def preform_operation(x, op, y):
  if op == "+":
    return int(x) + int(y)
  if op == "*":
    return int(x) * int(y)

def evalutate_line(line):
  split_exp = line.split(" ")
  try:
    plus_location = split_exp.index("+")
    x, op, y = split_exp[plus_location - 1], split_exp[plus_location], split_exp[plus_location + 1]
  except ValueError:
    x, op, y = split_exp[0], split_exp[1], split_exp[2]
  value = preform_operation(x, op, y)
  expression = line.replace(f"{x} {op} {y}", str(value), 1)
  return expression

def evalutate_exp(expression):
  while expression.count("(") > 0: #While there are any expressions with parentheses
    parentheses_expressions = re.findall(r"[(][\d *+]+[)]", expression) #Get them all
    for exp in parentheses_expressions: #For each one
      raw_expression = exp[1:-1] #Remove parentheses
      while raw_expression.count(" ") > 0: #While that expression has spaces (isnt one term)
        raw_expression = evalutate_line(raw_expression) #Evaluate the first two terms and replace the two terms with the new single term
      expression = expression.replace(exp, str(raw_expression), 1) #Replace the whole parenthesis expression with a single term
  while expression.count(" ") > 0:
    expression = evalutate_line(expression)
  print(expression)
  return int(expression)


total_sum = 0
for line in instructions:
  result = evalutate_exp(line)
  total_sum += result
  print(total_sum)

#29839238942436, too high.
#29839238838303, second try. 
# Was replacing every instance of the expression with the result, so 2*6 + 2 * 62 became (12) + (12)2
#201376568795521 PART2 FIRST TRY