import hashlib


for i in range(1000000):
  input = "yzbqklnj" + str(i)
  hash = hashlib.md5(input.encode())
  hex_code = hash.hexdigest()
  if hex_code[0:5] == "00000":
    print(i)
    break

