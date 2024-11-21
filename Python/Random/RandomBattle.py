import os
from colorama import Fore
import random
import time

#Get grid size
os.system("clear")
while True:
  Input = input("How large should the grid be?\n")
  if Input == "":
    Input = "20"
  if Input.isdigit() == False:
    os.system("clear")
    print("Please give a number.\n")
    continue
  Input = int(Input)
  if Input < 10:
    os.system("clear")
    print("Please give a grid size larger than or equal to 9.\n")
    continue
  GridSize = Input
  break

Grid = [[". " for x in range(GridSize+4)] for x in range(GridSize+4)]

################### FUNCTIONS ###################
def Print():
  String = "   1 2 3 "
  Counter = 2
  while Counter < (GridSize):
    Counter += 2
    Placeholder = str(Counter)
    while len(Placeholder) < 4:
      Placeholder = Placeholder + " "
    String = String + Placeholder
  print(Fore.WHITE + String)
  ####################################
  Counter = 0
  TotalString = ""
  First = True
  for ROW in Grid[2:-2]:
    Counter += 1
    if Counter < 10:
      String = Fore.WHITE + str(Counter) + Fore.WHITE + "  "
    else:
      String = Fore.WHITE + str(Counter) + Fore.WHITE + " "
    for COLUMN in ROW[2:-2]:
      if COLUMN == ". ":
        String += Fore.WHITE + COLUMN
      if COLUMN == "B":
        String += Fore.BLUE + "██"
      if COLUMN == "R":
        String += Fore.RED + "██"
    if First:
      TotalString += String + (Fore.WHITE + str(Counter))
      First = False
    else:
      TotalString += "\n" + String + (Fore.WHITE + str(Counter))
  print(TotalString)
  ####################################
  String = "   1 2 3 "
  Counter = 2
  while Counter < (GridSize):
    Counter += 2
    Placeholder = str(Counter)
    while len(Placeholder) < 4:
      Placeholder = Placeholder + " "
    String = String + Placeholder
  print(Fore.WHITE + String)
#################################################
def SmallPrint():
  TotalString = ""
  for ROW in Grid[2:-2]:
    String = Fore.WHITE + ""
    for COLUMN in ROW[2:-2]:
      if COLUMN == ". ":
        String += Fore.WHITE + COLUMN
      if COLUMN == "B":
        String += Fore.BLUE + "██"
      if COLUMN == "R":
        String += Fore.RED + "██"
    TotalString += "\n" + String
  print(TotalString)
################### FUNCTIONS ###################

#Setting alive squares
os.system("clear")
First = True
while True:
  Print()
  if First == False:
    print(Fore.RED + "Please give a valid input")
  First = False
  Input = input(Fore.WHITE + "What tile should be set to which color?\nType 'break' to stop changing tiles.")
  if Input == "break":
    break
  if Input.count(" ") != 2:
    os.system("clear")
    continue
  Input = Input.split()
  if (Input[0].lower() != "r" and Input[0].lower() != "b" and Input[0].lower() != "e") or Input[1].isdigit() == False or Input[2].isdigit() == False:
    os.system("clear")
    continue
  if Input[0].lower() == "e":
    Input[0] = ". "
  else:
    Input[0] = Input[0].upper()
  
  Input[1] = int(Input[1])
  Input[2] = int(Input[2])

  if max(Input[1], Input[2]) > GridSize:
    os.system("clear")
    continue

  Grid[Input[1]+1][Input[2]+1] = Input[0]
  First = True
  os.system("clear")

#Get how long sim should run
os.system("clear")
while True:
  Input = input("How long should the simulation run?\n")
  if Input.isdigit() == False:
    os.system("clear")
    print("Please input a number.")
    continue
  GameLoops = int(Input)
  break

for GAME_INSTANCE in range(GameLoops):
  NewGrid = [[". " for x in range(GridSize + 4)] for x in range(GridSize + 4)]
  Counter = 0
  for ROW in range(2, GridSize+2):
    for COLUMN in range(2, GridSize+2):
      Counter += 1
      BlueNeighbors = 0
      RedNeighbors = 0
      Current = Grid[ROW][COLUMN]
      if Grid[ROW+1][COLUMN] == "R":
        RedNeighbors += 1
      if Grid[ROW+1][COLUMN] == "B":
        BlueNeighbors += 1
      if Grid[ROW][COLUMN+1] == "R":
        RedNeighbors += 1
      if Grid[ROW][COLUMN+1] == "B":
        BlueNeighbors += 1
      if Grid[ROW-1][COLUMN] == "R":
        RedNeighbors += 1
      if Grid[ROW-1][COLUMN] == "B":
        BlueNeighbors += 1
      if Grid[ROW][COLUMN-1] == "R":
        RedNeighbors += 1
      if Grid[ROW][COLUMN-1] == "B":
        BlueNeighbors += 1
      if Counter % 2 == 0:
        if Current == "B":
          if NewGrid[ROW][COLUMN] == ". ":
            NewGrid[ROW][COLUMN] = "B"
          if RedNeighbors == 0:
            NewGrid[ROW][COLUMN] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW+1][COLUMN] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW-1][COLUMN] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW][COLUMN+1] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW][COLUMN-1] = "B"
          else:
            if Grid[ROW+1][COLUMN] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW+1][COLUMN] = "B"
            if Grid[ROW][COLUMN+1] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN+1] = "B"
            if Grid[ROW-1][COLUMN] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW-1][COLUMN] = "B"
            if Grid[ROW][COLUMN-1] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN-1] = "B"
        
        elif Current == "R":
          if NewGrid[ROW][COLUMN] == ". ":
            NewGrid[ROW][COLUMN] = "R"
          if BlueNeighbors == 0:
            RandomNumber = random.randint(1,10)
            NewGrid[ROW][COLUMN] = "R"
            if RandomNumber == 1:
              NewGrid[ROW+1][COLUMN] = "R"
            if RandomNumber == 2:
              NewGrid[ROW-1][COLUMN] = "R"
            if RandomNumber == 3:
              NewGrid[ROW][COLUMN+1] = "R"
            if RandomNumber == 4:
              NewGrid[ROW][COLUMN-1] = "R"
          else:
            if Grid[ROW+1][COLUMN] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW+1][COLUMN] = "R"
            if Grid[ROW][COLUMN+1] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN+1] = "R"
            if Grid[ROW-1][COLUMN] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW-1][COLUMN] = "R"
            if Grid[ROW][COLUMN-1] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN-1] = "R"
      else:
        if Current == "R":
          if NewGrid[ROW][COLUMN] == ". ":
            NewGrid[ROW][COLUMN] = "R"
          if BlueNeighbors == 0:
            RandomNumber = random.randint(1,10)
            NewGrid[ROW][COLUMN] = "R"
            if RandomNumber == 1:
              NewGrid[ROW+1][COLUMN] = "R"
            if RandomNumber == 2:
              NewGrid[ROW-1][COLUMN] = "R"
            if RandomNumber == 3:
              NewGrid[ROW][COLUMN+1] = "R"
            if RandomNumber == 4:
              NewGrid[ROW][COLUMN-1] = "R"
          else:
            if Grid[ROW+1][COLUMN] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW+1][COLUMN] = "R"
            if Grid[ROW][COLUMN+1] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN+1] = "R"
            if Grid[ROW-1][COLUMN] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW-1][COLUMN] = "R"
            if Grid[ROW][COLUMN-1] == "B":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN-1] = "R"
        elif Current == "B":
          if NewGrid[ROW][COLUMN] == ". ":
            NewGrid[ROW][COLUMN] = "B"
          if RedNeighbors == 0:
            NewGrid[ROW][COLUMN] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW+1][COLUMN] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW-1][COLUMN] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW][COLUMN+1] = "B"
            if random.randint(1,10) == 1:
              NewGrid[ROW][COLUMN-1] = "B"
          else:
            if Grid[ROW+1][COLUMN] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW+1][COLUMN] = "B"
            if Grid[ROW][COLUMN+1] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN+1] = "B"
            if Grid[ROW-1][COLUMN] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW-1][COLUMN] = "B"
            if Grid[ROW][COLUMN-1] == "R":
              if random.randint(1,10) == 1:
                NewGrid[ROW][COLUMN-1] = "B"
        
          
  Grid = []
  for x in NewGrid:
    Grid.append(x)
  time.sleep(.5)
  os.system("clear")
  SmallPrint()
  print(Fore.WHITE + str(GAME_INSTANCE))