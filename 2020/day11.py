import itertools

text = open("2020/day11.txt").read()

def step(text, seats): #Begin with a string of seats and floor
  #print(text)
  return_text = ""
  lines = text.splitlines() #Get a list of the lines to iterate through
  text = text.replace("\n", "") #Remove the newlines for iteration purposes

  seats_occupied = seats #Start with current seats occupied
  for row_index in range(len(lines)): #Row index = current row
    row = lines[row_index]

    for seat_index in range(len(row)): #Seat index = current seat
      seat_number = seat_index + len(row) * row_index #Get the seat index in all of the text
      seat = row[seat_index] #Find the actual value of that seat

      slopes = [(-1, -1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)] #The slopes to check
      actual_seats = []
      for slope in slopes:
        current_pos = [seat_index, row_index] #x, y of seat
        while True:
          current_pos[0] += slope[0] #Move by x of slope
          current_pos[1] += slope[1] #Move by y of slope
          if current_pos[0] < 0 or current_pos[0] >= len(row) or current_pos[1] < 0 or current_pos[1] >= len(lines): #if it is out of bounds, append an x
            actual_seats.append("x")
            break
          current_seat = current_pos[0] + current_pos[1] * len(row) #If in bounds, find the position
          if text[current_seat] == "#" or text[current_seat] == "L": #If it is either an open seat or a closed seat, append it and break
            actual_seats.append(text[current_seat])
            break

      number_of_occupied_adjacent_seats = actual_seats.count("#")
      #print(seat_number, actual_seats, number_of_occupied_adjacent_seats)
      if seat == ".": #If the space is a floor, keep it as a floor
        return_text += "."
      elif seat == "L" and number_of_occupied_adjacent_seats == 0: #If the seat is open and there are no occupied seats nearby, occupy it.
        return_text += "#"
        seats_occupied += 1
      elif seat == "#" and number_of_occupied_adjacent_seats >= 5: #If the seat is occupied and there are 4 or more adjacent seats, leave
        return_text += "L"
        seats_occupied -= 1
      elif seat == "L" and number_of_occupied_adjacent_seats >= 1: #If there is even 1 occupied seat near an open seat, keep it open
        return_text += "L"
      elif seat == "#" and number_of_occupied_adjacent_seats < 5: #If the occupied seats around an occupied seat are less than 4, keep sitting
        return_text += "#"
    return_text += "\n" #Add a newline after each line
  return return_text, seats_occupied

seats = 0
while True:
  text, seats_occupied = step(text, seats)
  print(seats_occupied)
  if seats_occupied == seats:
    print("FINISH")
    print(seats_occupied)
    break
  else:
    seats = seats_occupied

  