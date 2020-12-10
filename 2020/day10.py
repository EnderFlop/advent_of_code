import re
import itertools

with open("2020/day10.txt") as text:
  text = text.read().splitlines()
text = [int(i) for i in text]

def search_for_adapter(current_voltage):
  print(f"current_voltage = {current_voltage}")
  if current_voltage + 1 in text:
    current_voltage += 1
    acc = "one"
  elif current_voltage + 2 in text:
    current_voltage += 2
    acc = "two"
  elif current_voltage + 3 in text:
    current_voltage += 3
    acc = "three"
  return current_voltage, acc

current_voltage = 0
one_volt_count = 0
three_volt_count = 0

while current_voltage < max(text):
  current_voltage, acc = search_for_adapter(current_voltage)
  if acc == "one":
    print("adding 1 to voltage")
    one_volt_count += 1
  if acc == "three":
    print("adding 3 to voltage")
    three_volt_count += 1
  print(f"voltage currently {current_voltage}")
  print(f"one volt count = {one_volt_count}\nthree volt count = {three_volt_count}\n")
print("Final number is always 3 higher than highest adapter, difference of three. three_count += 1")
print(one_volt_count * (three_volt_count+1))

#NOT 2592

