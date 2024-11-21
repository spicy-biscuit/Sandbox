import os

os.system('clear')

print("How big should the square grid be?\nIf it's too big, and it won't fit on screen,\nand will also take longer to render.")
GridSize = input("")
if GridSize == "":
  GridSize = "20"
GridSize = int(GridSize)
Grid = [[". " for x in range(GridSize)] for y in range(GridSize)]
Grid[10][10] == "X " #Testing

def Print():
  for x in Grid:
    String = ""
    for y in x:
      String = String + str(y)
    print(String)

def Change(Point1X, Point1Y, Point2X, Point2Y):
  #Goal: Shift point1 based on point2
  #Sub-goal 1: if points are adjacent, do nothing
  XDifference = Point1X - Point2X
  YDifference = Point1Y - Point2Y
  if (XDifference == -1 or XDifference == 0 or XDifference == 1) and (YDifference == -1 or YDifference == 0 or YDifference == 1):
    return([Point1X, Point1Y])

  #Sub-goal 2: if points are in a line from each other, shift by 1 in one direction
  if XDifference == 0 and YDifference < 0:
    return([Point1X, Point1Y+1])
  if XDifference == 0 and YDifference > 0:
    return([Point1X, Point1Y-1])
  if YDifference == 0 and XDifference < 0:
    return([Point1X+1, Point1Y])
  if YDifference == 0 and XDifference > 0:
    return([Point1X-1, Point1Y])

  #Sub-goal 3: if points are not in a line from each other, shift diagonally
  if XDifference < 0 and YDifference < 0:
    return([Point1X+1, Point1Y+1])
  if XDifference < 0 and YDifference > 0:
    return([Point1X+1, Point1Y-1])
  if XDifference > 0 and YDifference < 0:
    return([Point1X-1, Point1Y+1])
  if XDifference > 0 and YDifference > 0:
    return([Point1X-1, Point1Y-1])

print(Change(0,0,2,2))
print(Change(Change(0,0,2,2)[0], Change(0,0,2,2)[1], 2, 2))
  
HEAD_X = 0
HEAD_Y = 0
ROPE1X = ROPE1Y = 0 #Attached to HEAD
ROPE2X = ROPE2Y = 0 #Attached to ROPE1
ROPE3X = ROPE3Y = 0 #Attached to ROPE2
ROPE4X = ROPE4Y = 0 #Attached to ROPE3
ROPE5X = ROPE5Y = 0 #Attached to ROPE4
ROPE6X = ROPE6Y = 0 #Attached to ROPE5
ROPE7X = ROPE7Y = 0 #Attached to ROPE6
ROPE8X = ROPE8Y = 0 #Attached to ROPE7
ROPE9X = ROPE9Y = 0 #Attached to ROPE8

#Apply points and draw grid
Grid[ROPE2Y][ROPE2X] = "2 "
Grid[ROPE1Y][ROPE1X] = "1 "
Grid[HEAD_Y][HEAD_X] = "O "
Print()

#Get Input Keys:
UP_COMMAND = input("What key should correspond to moving up?")
if UP_COMMAND != "":
  LEFT_COMMAND = input("What key should correspond to moving left?")
  DOWN_COMMAND = input("What key should correspond to moving down?")
  RIGHT_COMMAND = input("What key should correspond to moving right?")
else:
  UP_COMMAND = "w"
  LEFT_COMMAND = "a"
  DOWN_COMMAND = "s"
  RIGHT_COMMAND = "d"
  
while True:
  print("Which direction would you like to move in?\nType 'break' to exit.")
  print("Please use your chosen keys.")
  while True:
    Input = input()
    Input = Input.lower()
    Flag = False
    Flag2 = False
    if Input == "break":
      Flag = True
      break
    elif Input == UP_COMMAND:
      Direction = "up"
      if HEAD_Y == 0:
        Flag2 = True
      if Flag2 == False:
        Grid[HEAD_Y][HEAD_X] = ". "
        HEAD_Y -= 1
        break
    elif Input == DOWN_COMMAND:
      Direction = "down"
      if HEAD_Y == GridSize-1:
        Flag2 = True
      if Flag2 == False:
        Grid[HEAD_Y][HEAD_X] = ". "
        HEAD_Y += 1
        break
    elif Input == LEFT_COMMAND:
      Direction = "left"
      if HEAD_X == 0:
        Flag2 = True
      if Flag2 == False:
        Grid[HEAD_Y][HEAD_X] = ". "
        HEAD_X -= 1
        break
    elif Input == RIGHT_COMMAND:
      Direction = "right"
      if HEAD_X == GridSize-1:
        Flag2 = True
      if Flag2 == False:
        Grid[HEAD_Y][HEAD_X] = ". "
        HEAD_X += 1
        break
    else:
      print("Invalid input. Please use your chosen keys.")
      continue
    if Flag2:
      print("Invalid input. You cannot move off the board.")
  if Flag:
    break

  #Reset Grid
  Grid = [[". " for x in range(GridSize)] for y in range(GridSize)]
  
  #ApplyRules
  # ROPE1X, ROPE1Y = Change(ROPE1X, ROPE1Y, HEAD_X, HEAD_Y)[0], Change(ROPE1X, ROPE1Y, HEAD_X, HEAD_Y)[1]
  # ROPE2X, ROPE2Y = Change(ROPE2X, ROPE2Y, ROPE1X, ROPE1Y)[0], Change(ROPE2X, ROPE2Y, ROPE1X, ROPE1Y)[1]
  # ROPE3X, ROPE3Y = Change(ROPE3X, ROPE3Y, ROPE2X, ROPE2Y)[0], Change(ROPE3X, ROPE3Y, ROPE2X, ROPE2Y)[1]
  # ROPE4X, ROPE4Y = Change(ROPE4X, ROPE4Y, ROPE3X, ROPE3Y)[0], Change(ROPE4X, ROPE4Y, ROPE3X, ROPE3Y)[1]
  # ROPE5X, ROPE5Y = Change(ROPE5X, ROPE5Y, ROPE4X, ROPE4Y)[0], Change(ROPE5X, ROPE5Y, ROPE4X, ROPE4Y)[1]
  # ROPE6X, ROPE6Y = Change(ROPE6X, ROPE6Y, ROPE5X, ROPE5Y)[0], Change(ROPE6X, ROPE6Y, ROPE5X, ROPE5Y)[1]
  # ROPE7X, ROPE7Y = Change(ROPE7X, ROPE7Y, ROPE6X, ROPE6Y)[0], Change(ROPE7X, ROPE7Y, ROPE6X, ROPE6Y)[1]
  # ROPE8X, ROPE8Y = Change(ROPE8X, ROPE8Y, ROPE7X, ROPE7Y)[0], Change(ROPE8X, ROPE8Y, ROPE7X, ROPE7Y)[1]
  # ROPE9X, ROPE9Y = Change(ROPE9X, ROPE9Y, ROPE8X, ROPE8Y)[0], Change(ROPE9X, ROPE9Y, ROPE8X, ROPE8Y)[1]
  #Apply Rules option 2
  while True:
    ROPE9X, ROPE9Y = Change(ROPE9X, ROPE9Y, ROPE8X, ROPE8Y)[0], Change(ROPE9X, ROPE9Y, ROPE8X, ROPE8Y)[1]
    ROPE8X, ROPE8Y = Change(ROPE8X, ROPE8Y, ROPE7X, ROPE7Y)[0], Change(ROPE8X, ROPE8Y, ROPE7X, ROPE7Y)[1]
    ROPE7X, ROPE7Y = Change(ROPE7X, ROPE7Y, ROPE6X, ROPE6Y)[0], Change(ROPE7X, ROPE7Y, ROPE6X, ROPE6Y)[1]
    ROPE6X, ROPE6Y = Change(ROPE6X, ROPE6Y, ROPE5X, ROPE5Y)[0], Change(ROPE6X, ROPE6Y, ROPE5X, ROPE5Y)[1]
    ROPE5X, ROPE5Y = Change(ROPE5X, ROPE5Y, ROPE4X, ROPE4Y)[0], Change(ROPE5X, ROPE5Y, ROPE4X, ROPE4Y)[1]
    ROPE4X, ROPE4Y = Change(ROPE4X, ROPE4Y, ROPE3X, ROPE3Y)[0], Change(ROPE4X, ROPE4Y, ROPE3X, ROPE3Y)[1]
    ROPE3X, ROPE3Y = Change(ROPE3X, ROPE3Y, ROPE2X, ROPE2Y)[0], Change(ROPE3X, ROPE3Y, ROPE2X, ROPE2Y)[1]
    ROPE2X, ROPE2Y = Change(ROPE2X, ROPE2Y, ROPE1X, ROPE1Y)[0], Change(ROPE2X, ROPE2Y, ROPE1X, ROPE1Y)[1]
    ROPE1X, ROPE1Y = Change(ROPE1X, ROPE1Y, HEAD_X, HEAD_Y)[0], Change(ROPE1X, ROPE1Y, HEAD_X, HEAD_Y)[1]
    if [ROPE9X, ROPE9Y] == Change(ROPE9X, ROPE9Y, ROPE8X, ROPE8Y) and [ROPE8X, ROPE8Y] == Change(ROPE8X, ROPE8Y, ROPE7X, ROPE7Y) and [ROPE7X, ROPE7Y] == Change(ROPE7X, ROPE7Y, ROPE6X, ROPE6Y) and [ROPE6X, ROPE6Y] == Change(ROPE6X, ROPE6Y, ROPE5X, ROPE5Y) and [ROPE5X, ROPE5Y] == Change(ROPE5X, ROPE5Y, ROPE4X, ROPE4Y) and [ROPE4X, ROPE4Y] == Change(ROPE4X, ROPE4Y, ROPE3X, ROPE3Y) and [ROPE3X, ROPE3Y] == Change(ROPE3X, ROPE3Y, ROPE2X, ROPE2Y) and [ROPE2X, ROPE2Y] == Change(ROPE2X, ROPE2Y, ROPE1X, ROPE1Y) and [ROPE1X, ROPE1Y] == Change(ROPE1X, ROPE1Y, HEAD_X, HEAD_Y):
      break
  
  #Draw grid
  Grid[ROPE9Y][ROPE9X] = "██"
  Grid[ROPE8Y][ROPE8X] = "██"
  Grid[ROPE7Y][ROPE7X] = "██"
  Grid[ROPE6Y][ROPE6X] = "██"
  Grid[ROPE5Y][ROPE5X] = "██"
  Grid[ROPE4Y][ROPE4X] = "██"
  Grid[ROPE3Y][ROPE3X] = "██"
  Grid[ROPE2Y][ROPE2X] = "██"
  Grid[ROPE1Y][ROPE1X] = "██"
  Grid[HEAD_Y][HEAD_X] = "O "
  
  os.system('clear')
  Print()
  print("Cordinates:" + str(HEAD_X) + " " + str(HEAD_Y))
  print("Direction: " + str(Direction))
  print()