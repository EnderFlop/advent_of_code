import re

with open("2015/day7.txt") as text_file:
  instructions = text_file.read()
instructions = instructions.split("\n")

def AND(a,b):
  return a & b

def OR(a,b):
  return a | b

def NOT(a):
  return ~a

def LSHIFT(a,b):
  return a << b

def RSHIFT (a,b):
  return a >> b

def parse_instruction(instruction):
  command = "".join(re.findall("[A-Z]", instruction))
  args = re.findall(r"\w+", instruction.replace(command, ""))
  destination = args.pop()
  for index in range(len(args)):
    try:
      args[index] = int(args[index])
    except ValueError:
      continue
  return command, args, destination

wires = {}

def calculateWire(wire_name):
  wire = wires.get(wire_name, None)
  print(wire_name, wire)


  if isinstance(wire_name, int):
    print(f"returning {wire_name}")
    return wire_name
  if isinstance(wire, int):
    print(f"returning {wire}")
    return wire
  if wire is None:
    print(f"returning none")
    return None


  if len(wire["command"]) > 1:
    print(f"{wire['command']} in wire")
    if wire["command"] == "OR":
      wires[wire_name] = OR(calculateWire(wire["args"][0]), calculateWire(wire["args"][1]))
    elif wire["command"] == "AND":
      wires[wire_name] = AND(calculateWire(wire["args"][0]), calculateWire(wire["args"][1]))
    elif wire["command"] == "NOT":
      wires[wire_name] = NOT(calculateWire(wire["args"][0]))
    elif wire["command"] == "LSHIFT":
      wires[wire_name] = LSHIFT(calculateWire(wire["args"][0]), calculateWire(wire["args"][1]))
    elif wire["command"] == "RSHIFT":
      wires[wire_name] = RSHIFT(calculateWire(wire["args"][0]), calculateWire(wire["args"][1]))
  else:
    print(f"no command in wire")
    wires[wire_name] = calculateWire(wire["args"][0])

  return wires[wire_name]
    

for instruction in instructions:
  command, args, destination = parse_instruction(instruction)
  wires[destination] = {"command": command, "args": args}

print(calculateWire("a"))