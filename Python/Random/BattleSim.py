#Each side sets up foot soldier barracks and archer barracks
#fight based on rules

#Militia can attack within 2 tiles (10 hp, 4 dmg)
#Archers can attack within 4 tiles (4 hp, 8 dmg)
#if no enemy is in range, will just move towards enemy capital
#Capital does nothing but sit there with (20 hp)
#Baracks have (10 hp)
#Barracks will spawn a soldier in a spot adjacent to them, if there is room.

#Finished List:
#Setting up grid
#Format grid
#Placing barracks
#Placing archery ranges
#Spawning Troops
#Add restricting placement to home 5 rows

#To do List:
#Implement Alternating turns thing (two pointers, each one  taking turns advancing towards center, hits all points eventually, gives fair chance to both sides) (or just to the 2 range thing)
#Add capital placement
#Add detection for if enemy is in range
#Add attacking
#Add moving

import os
import colorama
from colorama import Fore

########### FUNCTIONS ###########
#################################

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
###################### Main ######################
  Counter = 0
  for x in Grid[4:-4]:
    Counter += 1
    if Counter < 10:
      String = Fore.WHITE + str(Counter) + Fore.WHITE + "  "
    else:
      String = Fore.WHITE + str(Counter) + Fore.WHITE + " "
    for y in x[4:-4]:
      if y == ". ":
        y = Fore.WHITE + ". "
      if type(y) == list:
        y = y[0]
      if y[0] == "B":
        y = Fore.BLUE + y[1] + " "
      if y[0] == "R":
        y = Fore.RED + y[1] + " "
      String = (String) + y
    print(String + (Fore.WHITE + str(Counter)))
###################### Main ######################
  String = "   1 2 3 "
  Counter = 2
  while Counter < (GridSize):
    Counter += 2
    Placeholder = str(Counter)
    while len(Placeholder) < 4:
      Placeholder = Placeholder + " "
    String = String + Placeholder
  print(Fore.WHITE + String)

########### FUNCTIONS ###########
#################################

#Intro
os.system('clear')
print("BattleSim is a small 'cellular autonama' game.\nMuch like John Conway's game of life, you set up the\nboard before hand, and watch the result play out.\n\nUnlike Conway's game, however, there are two players.\nEach player sets up 3 militia barracks and 1 archer barracks\non their side of the field (red on top, blue on bottom),\nbefore allowing the game to play.\n\nEach turn of the simulation, barracks spawn troops, and\ntroops will either attack an enemy piece, or move towards\nthe enemy capital.\n")
input("Press 'enter' to play.")


#Setting Grid
os.system("clear")
print(Fore.WHITE + "How big would you like the grid to be?")
while True:
  GridSize = input("")
  if GridSize == "":
    GridSize = "20"
  if GridSize.isdigit():
    GridSize = int(GridSize)
    if GridSize > 10:
      break
  os.system("clear")
  print(Fore.WHITE + "that wasn't a valid number. Please try again.\nHow big would you like the grid to be?")
Grid = [[(". ") for x in range(GridSize + 8)] for x in range(GridSize + 8)]

#Placing RED TEAM'S 3 militia barracks and 1 archer barrack and capital (limited)
os.system("clear")
for x in range(3):
  os.system("clear")
  while True:
    Print()
    print(Fore.RED + "Where would you like to place a Militia barrack?\nPlease format as 'Column Row'")
    Input = input()
    if Input.count(" ") != 1:
      os.system("clear")
      print(Fore.WHITE + "That was not a valid input. Please try again.")
      continue
    Input = Input.split()
    Flag = False
    for y in Input:
      if y.isdigit() == False:
        os.system("clear")
        print(Fore.WHITE + "Please input numbers.")
        Flag = True
        break
    if Flag:
      continue
        
    Input[0] = int(Input[0]) + 3
    Input[1] = int(Input[1]) + 3

    Flag = False
    if Input[0] <= 0 or Input[0] > GridSize+3 or Input[1] <= 0 or Input[1] > 8:
      os.system("clear")
      print(Fore.WHITE + "Please input a square in your zone.")
      Flag = True
    if Flag:
      continue
      
    Grid[Input[1]][Input[0]] = "RB"
    break

#Archer Range
for x in range(1):
  os.system("clear")
  while True:
    Print()
    print(Fore.RED + "Where would you like to place an Archer barrack?\nPlease format as 'Column Row'")
    Input = input()
    if Input.count(" ") != 1:
      os.system("clear")
      print(Fore.WHITE + "That was not a valid input. Please try again.")
      continue
    Input = Input.split()
    Flag = False
    for y in Input:
      if y.isdigit() == False:
        os.system("clear")
        print(Fore.WHITE + "Please input numbers.")
        Flag = True
        break
    if Flag:
      continue
        
    Input[0] = int(Input[0]) + 3
    Input[1] = int(Input[1]) + 3

    Flag = False
    if Input[0] <= 0 or Input[0] > GridSize+3 or Input[1] <= 0 or Input[1] > 8:
      os.system("clear")
      print(Fore.WHITE + "Please input a square on the grid.")
      Flag = True
      break
    if Flag:
      continue
      
    Grid[Input[1]][Input[0]] = "RR"
    break



#################################################
##---------------------------------------------##
#################################################
    
#Placing BLUE TEAM'S 3 militia barracks and 1 archer barrack
os.system("clear")
for x in range(3):
  os.system("clear")
  while True:
    Print()
    print(Fore.BLUE + "Where would you like to place a Militia barrack?\nPlease format as 'Column Row'")
    Input = input()
    if Input.count(" ") != 1:
      os.system("clear")
      print(Fore.WHITE + "That was not a valid input. Please try again.")
      continue
    Input = Input.split()
    Flag = False
    for y in Input:
      if y.isdigit() == False:
        os.system("clear")
        print(Fore.WHITE + "Please input numbers.")
        Flag = True
        break
    if Flag:
      continue
        
    Input[0] = int(Input[0]) + 3
    Input[1] = int(Input[1]) + 3

    Flag = False
    if Input[0] <= 0 or Input[0] > GridSize+3 or Input[1] <= GridSize+3-5 or Input[1] > GridSize+3:
      os.system("clear")
      print(Fore.WHITE + "Please input a square on the grid.")
      Flag = True
    if Flag:
      continue
      
    Grid[Input[1]][Input[0]] = "BB"
    break

#Archer Range
for x in range(1):
  os.system("clear")
  while True:
    Print()
    print(Fore.BLUE + "Where would you like to place an Archer barrack?\nPlease format as 'Column Row'")
    Input = input()
    if Input.count(" ") != 1:
      os.system("clear")
      print(Fore.WHITE + "That was not a valid input. Please try again.")
      continue
    Input = Input.split()
    Flag = False
    for y in Input:
      if y.isdigit() == False:
        os.system("clear")
        print(Fore.WHITE + "Please input numbers.")
        Flag = True
        break
    if Flag:
      continue
        
    Input[0] = int(Input[0]) + 3
    Input[1] = int(Input[1]) + 3

    Flag = False
    if Input[0] <= 0 or Input[0] > GridSize+3 or Input[1] <= GridSize+3-5 or Input[1] > GridSize+3:
      os.system("clear")
      print(Fore.WHITE + "Please input a square on the grid.")
      Flag = True
    if Flag:
      continue
      
    Grid[Input[1]][Input[0]] = "BR"
    break
    
#################################################
##----------------- GAME LOOP -----------------##
#################################################

while True:
  Print()
  for ROW in range(4, GridSize+3):
    for COLUMN in range(4, GridSize+3):
      
#################################################
##-------------- SPAWNING TROOPS --------------##
#################################################
      
      #Blue Team - Militia Barracks
      if Grid[ROW][COLUMN] == "BB":
        #check all spots around, make sure not offscreen
        if (Grid[ROW-1][COLUMN] == ". " or Grid[ROW-1][COLUMN] == Fore.WHITE + ". ") and ROW != 4:
          Grid[ROW-1][COLUMN] = ["BM", 10]
        elif (Grid[ROW][COLUMN-1] == ". " or Grid[ROW][COLUMN-1] == Fore.WHITE + ". ") and COLUMN != 4:
          Grid[ROW][COLUMN-1] = ["BM", 10]
        elif (Grid[ROW][COLUMN+1] == ". " or Grid[ROW][COLUMN+1] == Fore.WHITE + ". ") and COLUMN != GridSize+3:
          Grid[ROW][COLUMN+1] = ["BM", 10]
        elif (Grid[ROW+1][COLUMN] == ". " or Grid[ROW+1][COLUMN] == Fore.WHITE + ". ") and ROW != GridSize+3:
          Grid[ROW+1][COLUMN] = ["BM", 10]
      #Blue Team - Archer Barracks
      if Grid[ROW][COLUMN] == "BR":
        #check all spots around, make sure not offscreen
        if (Grid[ROW-1][COLUMN] == ". " or Grid[ROW-1][COLUMN] == Fore.WHITE + ". ") and ROW != 4:
          Grid[ROW-1][COLUMN] = ["BA", 10]
        elif (Grid[ROW][COLUMN-1] == ". " or Grid[ROW][COLUMN-1] == Fore.WHITE + ". ") and COLUMN != 4:
          Grid[ROW][COLUMN-1] = ["BA", 10]
        elif (Grid[ROW][COLUMN+1] == ". " or Grid[ROW][COLUMN+1] == Fore.WHITE + ". ") and COLUMN != GridSize+3:
          Grid[ROW][COLUMN+1] = ["BA", 10]
        elif (Grid[ROW+1][COLUMN] == ". " or Grid[ROW+1][COLUMN] == Fore.WHITE + ". ") and ROW != GridSize+3:
          Grid[ROW+1][COLUMN] = ["BA", 10]

      #Red Team - Militia Barracks
      if Grid[ROW][COLUMN] == "RB":
        #check all spots around, make sure not offscreen
        if (Grid[ROW+1][COLUMN] == ". " or Grid[ROW+1][COLUMN] == Fore.WHITE + ". ") and ROW != GridSize+3:
          Grid[ROW+1][COLUMN] = ["RM", 10]
        elif (Grid[ROW][COLUMN-1] == ". " or Grid[ROW][COLUMN-1] == Fore.WHITE + ". ") and COLUMN != 4:
          Grid[ROW][COLUMN-1] = ["RM", 10]
        elif (Grid[ROW][COLUMN+1] == ". " or Grid[ROW][COLUMN+1] == Fore.WHITE + ". ") and COLUMN != GridSize+3:
          Grid[ROW][COLUMN+1] = ["RM", 10]
        elif (Grid[ROW-1][COLUMN] == ". " or Grid[ROW-1][COLUMN] == Fore.WHITE + ". ") and ROW != 4:
          Grid[ROW-1][COLUMN] = ["RM", 10]
      #Red Team - Archer Barracks
      if Grid[ROW][COLUMN] == "RR":
        #check all spots around, make sure not offscreen
        if (Grid[ROW+1][COLUMN] == ". " or Grid[ROW+1][COLUMN] == Fore.WHITE + ". ") and ROW != GridSize+3:
          Grid[ROW+1][COLUMN] = ["RA", 10]
        elif (Grid[ROW][COLUMN-1] == ". " or Grid[ROW][COLUMN-1] == Fore.WHITE + ". ") and COLUMN != 4:
          Grid[ROW][COLUMN-1] = ["RA", 10]
        elif (Grid[ROW][COLUMN+1] == ". " or Grid[ROW][COLUMN+1] == Fore.WHITE + ". ") and COLUMN != GridSize+3:
          Grid[ROW][COLUMN+1] = ["RA", 10]
        elif (Grid[ROW-1][COLUMN] == ". " or Grid[ROW-1][COLUMN] == Fore.WHITE + ". ") and ROW != 4:
          Grid[ROW-1][COLUMN] = ["RA", 10]
          
#################################################
##--------------- MOVING TROOPS ---------------##
#################################################
  
  break #Testing
Print()