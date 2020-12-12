import itertools

text = open("2020/day11.txt").read()

def step(text, seats): #Begin with a string of seats and floor
  #print(text)
  return_text = ""
  lines = text.splitlines() #Get a list of the lines to iterate through
  text = text.replace("\n", "") #Remove the newlines for iteration purposes
  board = "" #Long string that is used for index lookup of characters without needing to worry about newlines
  for i in lines:
    board += i

  seats_occupied = seats #Start with current seats occupied
  for row_index in range(len(lines)): #Row index = current row
    row = lines[row_index]

    for seat_index in range(len(row)): #Seat index = current seat
      seat_number = seat_index + len(row) * row_index #Get the seat index in all of the text
      seat = row[seat_index] #Find the actual value of that seat

      higher_row = [seat_number - len(row) - 1, seat_number - len(row), seat_number - len(row) + 1]
      middle_row = [seat_number - 1, seat_number + 1] 
      lower_row = [seat_number + len(row) - 1, seat_number + len(row), seat_number + len(row) + 1]

      actual_seats = []
      for i in higher_row:
        #Current problem. if your lower row is indexes 2,3,4 and the lines look like
        # 0,1,2
        # 3,4,5
        # It will steal the value from the previous line instead of adding a period.
        # SOLUTION: Impliment different checks for each row, using their row as a range check
        # Add a check that i is in the current row by checking if i is in a range, starting with the current row's first index and ending with it's last
        if i >= 0 and i < len(text) and i in range(len(row) * (row_index - 1), len(row) * row_index):
          actual_seats.append(text[i])
        else:
          actual_seats.append(".")
      for i in middle_row:
        if i >= 0 and i < len(text) and i in range(len(row) * row_index, len(row) * (row_index + 1)):
          actual_seats.append(text[i])
        else:
          actual_seats.append(".")
      for i in lower_row:
        if i >= 0 and i < len(text) and i in range(len(row) * (row_index + 1), len(row) * (row_index + 2)):
          actual_seats.append(text[i])
        else:
          actual_seats.append(".")

      number_of_occupied_adjacent_seats = actual_seats.count("#")
      #print(seat_number, actual_seats, number_of_occupied_adjacent_seats)
      if seat == ".": #If the space is a floor, keep it as a floor
        return_text += "."
      elif seat == "L" and number_of_occupied_adjacent_seats == 0: #If the seat is open and there are no occupied seats nearby, occupy it.
        return_text += "#"
        seats_occupied += 1
      elif seat == "#" and number_of_occupied_adjacent_seats >= 4: #If the seat is occupied and there are 4 or more adjacent seats, leave
        return_text += "L"
        seats_occupied -= 1
      elif seat == "L" and number_of_occupied_adjacent_seats >= 1: #If there is even 1 occupied seat near an open seat, keep it open
        return_text += "L"
      elif seat == "#" and number_of_occupied_adjacent_seats < 4: #If the occupied seats around an occupied seat are less than 4, keep sitting
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

  