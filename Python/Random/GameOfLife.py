import os
import timeit
import time

#Setting Grid
os.system("clear")
print("How big would you like the grid to be?")
while True:
  GridSize = input("")
  if GridSize == "":
    GridSize = "20"
  if GridSize.isdigit():
    GridSize = int(GridSize)
    if GridSize > 0:
      break
  os.system("clear")
  print(
    "that wasn't a valid number. Please try again.\nHow big would you like the grid to be?")
Grid = [[(". ") for x in range(GridSize + 2)] for x in range(GridSize + 2)]

#Setting Game Type
os.system("clear")
while True:
  print("Which sim type would you like?\nConway's game of life - '1'\nSeeds - '2'")
  Input = input()
  if Input != "1" and Input != "2":
    os.system("clear")
    print("That wasn't an option. Try again.")
    continue
  else:
    GAME_TYPE = Input
    break

########### FUNCTIONS ###########
#################################

def Print():
  for x in Grid[1:-1]:
    String = ""
    for y in x[1:-1]:
      String = String + y
    print(String)

########### FUNCTIONS ###########
#################################

#Setting alive squares
while True:
  os.system("clear")
  First = True
  Flag = False
  while True:
    Print()
    if First == False:
      print("That was an invalid input. Try again.")
    First = False
    print(
      "What square would you like to flip?\nType 'continue' to stop changing tiles."
    )
    Input = input("")
    if Input == "continue":
      Flag = True
      break
    if Input.count(" ") != 1:
      os.system("clear")
      continue
    Input = Input.split()
    if Input[0].isdigit() == False or Input[1].isdigit() == False:
      os.system("clear")
      continue
    Input[0] = int(Input[0])
    Input[1] = int(Input[1])
    if int(Input[0]) < 0 or int(Input[0]) >= GridSize or int(
        Input[1]) < 0 or int(Input[1]) >= GridSize:
      os.system("clear")
      continue
    if Grid[Input[1]][Input[0]] == ". " or Grid[Input[1]][Input[0]] == ". ":
      Grid[Input[1]][Input[0]] = "██"
    elif Grid[Input[1]][Input[0]] == "██":
      Grid[Input[1]][Input[0]] = ". "
    break
  if Flag:
    break

#Ask how long simulation should run
while True:
  print("How many turns should the sim run?")
  Input = input()
  if Input.isdigit() == False:
    os.system("clear")
    print("Please input a number.")
    continue
  Input = int(Input)
  if Input < 1:
    os.system("clear")
    print("Please input a positive number.")
    continue
  RUNTIME = Input
  break

#Running the simulation
Counter = 0
while True:
  START = timeit.default_timer()
  NewGrid = [[". " for x in range(GridSize + 2)] for x in range(GridSize + 2)]
  for ROW in range(1,len(NewGrid)-1):
    for COLUMN in range(1, len(NewGrid)-1):
      Neighbors = 0
      if Grid[ROW-1][COLUMN-1] == "██":
        Neighbors += 1
      if Grid[ROW-1][COLUMN] == "██":
        Neighbors += 1
      if Grid[ROW-1][COLUMN+1] == "██":
        Neighbors += 1
      if Grid[ROW][COLUMN-1] == "██":
        Neighbors += 1
      if Grid[ROW][COLUMN+1] == "██":
        Neighbors += 1
      if Grid[ROW+1][COLUMN-1] == "██":
        Neighbors += 1
      if Grid[ROW+1][COLUMN] == "██":
        Neighbors += 1
      if Grid[ROW+1][COLUMN+1] == "██":
        Neighbors += 1

################## Apply Rules ##################
#################################################

      #Conway's game of life
      if GAME_TYPE == "1":
        if Neighbors == 3 or (Neighbors == 2 and Grid[ROW][COLUMN] == "██"):
          NewGrid[ROW][COLUMN] = "██"
        else:
          NewGrid[ROW][COLUMN] = ". "

      #Seeds
      if GAME_TYPE == "2":
        if Neighbors == 2 and Grid[ROW][COLUMN] == ". ":
          NewGrid[ROW][COLUMN] = "██"
        else:
          NewGrid[ROW][COLUMN] = ". "

################## Apply Rules ##################
#################################################
  
  Grid = []
  for x in NewGrid:
    Grid.append(x)
  END = timeit.default_timer()
  TIME = END - START
  os.system("clear")
  Print()
  time.sleep(1 - TIME)
  Counter += 1
  if Counter >= RUNTIME:
    break