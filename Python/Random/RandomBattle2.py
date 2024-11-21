import os
import colorama
from colorama import Fore
import time
import timeit
import random

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
  Input = input(Fore.WHITE + "What tile should be set to which color?\nType 'break' to stop changing tiles.\nType the first letter of the color, or e to set to an empty square.\nThen type the coordinates of the square(starting with row)\nExample: r 1 2")
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

def Opposite(String):
  if String == "r":
    return("b")
  return("r")

###################################
########     GAME LOOP     ########
###################################



for GAME_INSTANCE in range(GameLoops):
  BlueTiles = 0  #To count number of each side
  RedTiles = 0   #To count number of each side
  START = timeit.default_timer()
  NewGrid = [[". " for x in range(GridSize + 4)] for x in range(GridSize + 4)]
  for ROW in range(2, GridSize+2):
    for COLUMN in range(2, GridSize+2):
      Current = Grid[ROW][COLUMN]
      Enemies = 0

      if Current != "e":
        if Grid[ROW+1][COLUMN] != Current and Grid[ROW+1][COLUMN] != "e":
          Enemies += 1
        if Grid[ROW-1][COLUMN] != Current and Grid[ROW-1][COLUMN] != "e":
          Enemies += 1
        if Grid[ROW][COLUMN+1] != Current and Grid[ROW][COLUMN+1] != "e":
          Enemies += 1
        if Grid[ROW][COLUMN-1] != Current and Grid[ROW][COLUMN-1] != "e":
          Enemies += 1

        if Enemies == 0:
          NewGrid[ROW][COLUMN] = Current
        if Enemies == 1:
          if random.randint(1,10) == 1:
            NewGrid[ROW][COLUMN] = Opposite(Current)
          else:
            NewGrid[ROW][COLUMN] = Current
        if Enemies == 2:
          if random.randint(1,4) == 1:
            NewGrid[ROW][COLUMN] = Opposite(Current)
          else:
            NewGrid[ROW][COLUMN] = Current
        if Enemies == 3:
          if random.randint(1,2) == 1:
            NewGrid[ROW][COLUMN] = Opposite(Current)
          else:
            NewGrid[ROW][COLUMN] = Current
        if Enemies == 4:
          NewGrid[ROW][COLUMN] = Opposite(Current)

      if Current == "e":
        BlueAdjacents = 0
        RedAdjacents = 0
        if Grid[ROW+1][COLUMN] == "b":
          BlueAdjacents += 1
        if Grid[ROW+1][COLUMN] == "r":
          RedAdjacents += 1
        if Grid[ROW-1][COLUMN] == "b":
          BlueAdjacents += 1
        if Grid[ROW-1][COLUMN] == "r":
          RedAdjacents += 1
        if Grid[ROW][COLUMN+1] == "b":
          BlueAdjacents += 1
        if Grid[ROW][COLUMN+1] == "r":
          RedAdjacents += 1
        if Grid[ROW][COLUMN-1] == "b":
          BlueAdjacents += 1
        if Grid[ROW][COLUMN-1] == "r":
          RedAdjacents += 1

        #roll d6 for each adjacent of that color, whoever has higher max wins
        #the tile. if its a tie, take a coinflip for winner. Must beat 3 to
        #take the tile
          
        BlueRolls = [0]
        RedRolls = [0]
        for x in range(BlueAdjacents):
          BlueRolls.append(random.randint(1, 6))
        for x in range(RedAdjacents):
          RedRolls.append(random.randint(1, 6))
        BlueValue = max(BlueRolls)
        RedValue = max(RedRolls)
        if BlueValue < 4 and RedValue < 4:
          NewGrid[ROW][COLUMN] = "e"
        elif BlueValue > RedValue:
          NewGrid[ROW][COLUMN] = "b"
        elif RedValue > BlueValue: 
          NewGrid[ROW][COLUMN] = "r"
        else:
          NewGrid[ROW][COLUMN] = "e"