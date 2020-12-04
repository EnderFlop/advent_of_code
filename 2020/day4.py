import re

with open("2020/day4.txt") as text_file:
  passports = text_file.read()

valid_ports = 0

passports = passports.split("\n\n")
for passport in passports:
  #print(passport)

  fields = re.findall(r"[a-zA-Z0-9#]+", passport)
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
  for key, value in fields_dict.items():
    if key == "byr":
      if int(value) >= 1920 and int(value) <= 2002:
        expected_fields.remove(key)
    elif key == "iyr":
      if int(value) >= 2010 and int(value) <= 2020:
        expected_fields.remove(key)
    elif key == "eyr":
      if int(value) >= 2020 and int(value) <= 2030:
        expected_fields.remove(key)
    elif key == "hgt":
      try:
        unit = re.search("[a-z]+", value).group()
        height = int(re.search("[0-9]+", value).group())
      except AttributeError:
        continue
      if unit == "cm":
        if height >= 150 and height <= 193:
          expected_fields.remove(key)
      elif unit == "in":
        if height >= 59 and height <= 76:
          expected_fields.remove(key)
    elif key == "hcl":
      regex = re.findall(r"#[0-9a-f]{6}$", value)
      if regex:
        expected_fields.remove(key)
    elif key == "ecl":
      if value in ["amb","blu","brn","gry","grn","hzl","oth"]:
        expected_fields.remove(key)
    elif key == "pid":
      regex = re.findall(r"^[0-9]{9}$", value)
      if regex:
        expected_fields.remove(key)
    elif key == "cid":
      continue
  if len(expected_fields) == 0 or expected_fields == ["cid"]:
    print(f"PASSED: \n{passport} \n{fields} \n{expected_fields}")
    valid_ports += 1
  else:
    #print(f"FAILED: \n{passport} \n{fields} \n{expected_fields}")
    continue
print(valid_ports)
  