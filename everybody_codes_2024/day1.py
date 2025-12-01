with open("day1.txt") as file:
  text = file.read()

enemies = {"A": 0, "B": 1, "C":3, "D":5, "x": 0}

def main():
  potions = 0
  i = 0
  while i < len(text) - 2:

    round_potions = 0
    monsters = text[i:i + 3]
    

    #add monster values
    for m in monsters:
      round_potions += enemies[m]

    #add extra potions for multi battles
    count = monsters.count("x")
    if count == 1:
      round_potions += 2
    if count == 0:
      round_potions += 6

    print(round_potions)

    potions += round_potions
    i += 3
  
  return potions
      





if __name__ == "__main__":
  res = main()
  print(res)