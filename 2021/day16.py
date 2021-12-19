import re
import itertools
import numpy as np
import time

instructions = open("2021/day16testinput.txt").read().splitlines()
#instructions = open("2021/day16input.txt").read().splitlines()



def binary_to_decimal(bin): #takes string, returns int
  return int(bin, 2)

def hexadecimal_to_binary(hex): #takes string, returns string
  integer = int(hex, 16)
  binary = format(integer, f"0>{4*len(hex)}b")
  return binary

def process_literal_packet(packet):
  packet_contents = ""
  for i in range(0, len(packet), 5):
    group_prefix = int(packet[i])
    group = packet[i+1:i+5]
    packet_contents += group
    if group_prefix == 0:
      break
  return packet_contents

def process_packet(packet):
  print(packet)
  global total_version_numbers
  packet_version = binary_to_decimal(packet[0:3])
  packet_id = binary_to_decimal(packet[3:6])
  length_type_id = int(packet[6])
  packet = packet[7:]
  total_version_numbers += packet_version

  #the current code will never recieve a literal unless it is the original packet (which is isn't)

  if length_type_id == 0: #the next 15 bits identify the length of the subpacket region to scan.
    length_of_subpacket = binary_to_decimal(packet[0:15])
    subpackets = packet[15:15+length_of_subpacket]
    #subpackets are 6 digits of metadata, then groups. 
    #find the metadata of the first packet. if it is literal, process and move to the next packet.
    #if it is not, recurse using that subpacket.
    while len(subpackets) > 0 and binary_to_decimal(subpackets) != 0:
      sub_version = binary_to_decimal(subpackets[0:3])
      sub_id = binary_to_decimal(subpackets[3:6])
      current_sub = subpackets[6:]
      if sub_id == 4: #if it is 4,
        print(f"literal version number:{sub_version}")
        print(current_sub)
        total_version_numbers += sub_version
        literal = process_literal_packet(current_sub)
        #if literal is 4 digits long, that means we sliced off one group identifier, 4 is 5, 8 is 10, 12 is 15, etc.
        literal_length = len(literal) + (len(literal) // 4)
        subpackets = subpackets[6 + literal_length:]
      elif sub_id != 4:
        process_packet(subpackets)

  if length_type_id == 1: #the next 11 bits indentify the number of subpackets in the rest of the packet.
    number_of_subpackets = binary_to_decimal(packet[0:11])
    subpackets = packet[11:]
    subs_processed = 0
    while subs_processed != number_of_subpackets:
      sub_version = binary_to_decimal(subpackets[0:3])
      sub_id = binary_to_decimal(subpackets[3:6])
      current_sub = subpackets[6:]
      if sub_id == 4:
        total_version_numbers += sub_version
        literal = process_literal_packet(current_sub)
        #if literal is 4 digits long, that means we sliced off one group identifier, 4 is 5, 8 is 10, 12 is 15, etc.
        literal_length = len(literal) + (len(literal) // 4)
        subpackets = subpackets[6 + literal_length:]
      elif sub_id != 4:
        process_packet(subpackets)
      subs_processed += 1

  print(f"current_ver:{packet_version} total_ver:{total_version_numbers}")
  return total_version_numbers

x = hexadecimal_to_binary("620080001611562C8802118E34")
global total_version_numbers
total_version_numbers = 0
print(process_packet(x))
#have to process the recursion differently. right now it needs to act differently based on length_type_id differences. figure it out :)
  