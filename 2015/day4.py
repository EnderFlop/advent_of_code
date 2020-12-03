import hashlib


for i in range(1000000000000000):
  input = "yzbqklnj" + str(i)
  hash = hashlib.md5(input.encode())
  hex_code = hash.hexdigest()
  if hex_code[0:6] == "000000":
    print(i)
    break

