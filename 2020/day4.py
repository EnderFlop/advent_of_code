import re

with open("day4.txt") as text_file:
  passports = text_file.read()

valid_ports = 0

passports = passports.split("\n\n")
for passport in passports:
  #print(passport)

  fields = re.findall(r"\w+", passport)
  fields_dict = {}
  for i in range(0, len(fields), 2):
    fields_dict[fields[i]] = fields[i+1]
  print(fields_dict)
  expected_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
  ]
  for key in fields_dict.keys():
    expected_fields.remove(key)
  if len(expected_fields) == 0 or expected_fields == ["cid"]:
    print(f"PASSED: \n{passport} \n{fields} \n{expected_fields}")
    valid_ports += 1
  else:
    #print(f"FAILED: \n{passport} \n{fields} \n{expected_fields}")
    continue
print(valid_ports)
  