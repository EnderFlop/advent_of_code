with open("2015/day7.txt") as text_file:
  instructions = text_file.read()

wires_dict = {}

instructions = instructions.split("\n")
for instruction in instructions:
  split_instruction = instruction.split()

  target_wire = split_instruction[-1]

  if instruction == "0 -> c":
    wires_dict["c"] = 0
    continue
  elif instruction == "1674 -> b":
    wires_dict["b"] = 1674
    continue
  elif instruction == "lx -> a": 
    if "lx" in wires_dict:
      wires_dict["a"] = wires_dict["lx"]
    continue
  
  elif split_instruction[0][0].isupper(): 
    if split_instruction[1] in wires_dict:
      wires_dict[target_wire] = ~ wires_dict[split_instruction[1]]

  elif split_instruction[0][0].islower() or split_instruction[0] == "1":
    first_signal_wire = split_instruction[0]
    command = split_instruction[1]
    second_signal_wire = split_instruction[2]
    if command == "AND":
      if first_signal_wire in wires_dict and second_signal_wire in wires_dict:
        wires_dict[target_wire] = first_signal_wire & second_signal_wire
    elif command == "OR":
      if first_signal_wire in wires_dict and second_signal_wire in wires_dict:
        wires_dict[target_wire] = first_signal_wire | second_signal_wire
    elif command == "RSHIFT":
      if first_signal_wire in wires_dict:
        wires_dict[target_wire] = first_signal_wire >> second_signal_wire #s_s_w in this case is a number to shift by
    elif command == "LSHIFT":
      if second_signal_wire in wires_dict:
        print
        wires_dict[target_wire] = first_signal_wire << second_signal_wire #s_s_w in this case is a number to shift by

print(wires_dict)


    
