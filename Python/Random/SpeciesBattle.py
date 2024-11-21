import os
import colorama
from colorama import Fore
import time
import timeit

TIE_BREAKER = "R"

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

#Get how often grid prints
os.system("clear")
while True:
  Input = input("How often should the grid be updated?\n")
  if Input == "":
    Input = "1"
  if Input.isdigit() == False:
    os.system("clear")
    print("Please give a number.\n")
    continue
  REPEATS_BEFORE_REFRESH = int(Input)
  TIME_COUNTER = 0
  break

#Get game type
os.system("clear")
while True:
  Possibles = ["1", "2", "3"]
  Input = input("What version of the game should be ran?\n1 - Original (looks very good with symetrical inputs)\n2 - New state is based on sum of ally and opponent pieces\n(works best for asymetrical inputs)\n3 - New state is based completly on if there are more red or blue neighbors. Works best with random inputs.\nCould be played as a game (take turns placing tiles, whoever ends up with more wins.)\n")
  if Input == "":
    Input = "1"
  if Input not in Possibles:
    os.system("clear")
    print("That is not an option. Try again.")
    continue
  GAME_TYPE = Input
  break

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

Print()

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
    
  
#################################################
##----------------- Game Loop -----------------##
#################################################

def GetNeighbors(ROW, COLUMN):
  RedNeighbors = 0
  BlueNeighbors = 0
  Current = Grid[ROW][COLUMN]
  Temp = Grid[ROW-1][COLUMN-1]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW-1][COLUMN]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW-1][COLUMN+1]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW][COLUMN-1]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW][COLUMN+1]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW+1][COLUMN-1]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW+1][COLUMN]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  Temp = Grid[ROW+1][COLUMN+1]
  if Temp == "R":
    RedNeighbors += 1
  if Temp == "B":
    BlueNeighbors += 1
  return([BlueNeighbors, RedNeighbors])

for GAME_INSTANCE in range(GameLoops):
  BlueTiles = 0  #To count number of each side
  RedTiles = 0   #To count number of each side
  START = timeit.default_timer()
  NewGrid = [[". " for x in range(GridSize + 4)] for x in range(GridSize + 4)]
  for ROW in range(2, GridSize+2):
    for COLUMN in range(2, GridSize+2):
      if Grid[ROW][COLUMN] == "B":
        BlueTiles += 1
      if Grid[ROW][COLUMN] == "R":
        RedTiles += 1
      BlueNeighbors = GetNeighbors(ROW, COLUMN)[0]
      RedNeighbors = GetNeighbors(ROW, COLUMN)[1]
      
#################################################
      #Normal Rules
      if GAME_TYPE == "1":
        #Is alive
        if Grid[ROW][COLUMN] == "R":
          if RedNeighbors == 2 or RedNeighbors == 3:
            NewGrid[ROW][COLUMN] = "R"
          else:
            NewGrid[ROW][COLUMN] = ". "
        elif Grid[ROW][COLUMN] == "B":
          if BlueNeighbors == 2 or BlueNeighbors == 3:
            NewGrid[ROW][COLUMN] = "B"
          else:
            NewGrid[ROW][COLUMN] = ". "
        #Has 2 or 1 neighbor(s) of both
        elif (RedNeighbors == 2 and BlueNeighbors == 2) or (RedNeighbors == 1 and BlueNeighbors == 1):
          if (TIE_BREAKER == "R" and BlueNeighbors == 0) or (TIE_BREAKER == "B" and RedNeighbors == 0):
            NewGrid[ROW][COLUMN] = TIE_BREAKER
          if TIE_BREAKER == "R":
            TIE_BREAKER = "B"
          else:
            TIE_BREAKER = "R"
        #Has neighbors of only Red
        elif (RedNeighbors == 2 or RedNeighbors == 1) and BlueNeighbors == 0:
          NewGrid[ROW][COLUMN] = "R"
        #Has neighbors of only Blue
        elif (BlueNeighbors == 2 or BlueNeighbors == 1) and RedNeighbors == 0:
          NewGrid[ROW][COLUMN] = "B"
        else:
          NewGrid[ROW][COLUMN] = ". "
        
#################################################
      #Alternate 1 (Allies)
      if GAME_TYPE == "2":
        if Grid[ROW][COLUMN] == "R":
          Neighbors = RedNeighbors - BlueNeighbors
          if Neighbors > 0:
            NewGrid[ROW][COLUMN] = "R"
          else:
            NewGrid[ROW][COLUMN] = ". "
          if RedNeighbors != 2 and RedNeighbors != 3:
            NewGrid[ROW][COLUMN] = ". "
        elif Grid[ROW][COLUMN] == "B":
          Neighbors = BlueNeighbors - RedNeighbors
          if Neighbors > 0:
            NewGrid[ROW][COLUMN] = "B"
          else:
            NewGrid[ROW][COLUMN] = ". "
          if BlueNeighbors != 2 and BlueNeighbors != 3:
            NewGrid[ROW][COLUMN] = ". "
        #Has 2 or 1 neighbor(s) of both
        elif (RedNeighbors == 2 and BlueNeighbors == 2) or (RedNeighbors == 1 and BlueNeighbors == 1):
          if (TIE_BREAKER == "R" and BlueNeighbors == 0) or (TIE_BREAKER == "B" and RedNeighbors == 0):
            NewGrid[ROW][COLUMN] = TIE_BREAKER
          if TIE_BREAKER == "R":
            TIE_BREAKER = "B"
          else:
            TIE_BREAKER = "R"
        #Has neighbors of only Red
        elif (RedNeighbors == 2 or RedNeighbors == 1) and BlueNeighbors == 0:
          NewGrid[ROW][COLUMN] = "R"
        #Has neighbors of only Blue
        elif (BlueNeighbors == 2 or BlueNeighbors == 1) and RedNeighbors == 0:
          NewGrid[ROW][COLUMN] = "B"
        else:
          NewGrid[ROW][COLUMN] = ". "
        
#################################################
      #New state is based completely on if you have more red or more blue neighbors.
      if GAME_TYPE == "3":
        if RedNeighbors > BlueNeighbors:
          NewGrid[ROW][COLUMN] = "R"
        if BlueNeighbors > RedNeighbors:
          NewGrid[ROW][COLUMN] = "B"
        if BlueNeighbors == RedNeighbors:
          NewGrid[ROW][COLUMN] = Grid[ROW][COLUMN]
        
#################################################
  Grid = []
  for x in NewGrid:
    Grid.append(x)
  TIME_COUNTER += 1
  if TIME_COUNTER == REPEATS_BEFORE_REFRESH:
    END = timeit.default_timer()
    time.sleep((REPEATS_BEFORE_REFRESH*0.005 + 0.5)-(END-START))
    END = timeit.default_timer()
    os.system("clear")
    SmallPrint()
    print(Fore.WHITE + str(GAME_INSTANCE))
    print("Red Tiles: " + str(RedTiles) + "\nBlue Tiles: " + str(BlueTiles))
    TIME_COUNTER = 0