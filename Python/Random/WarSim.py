#both players set up their side
#after that its a cellular autonama, with soldiers and buildings
#buildings produce soldiers near them, soldiers randomly move, and other buildings like farms create resources for barracks
#Capital is something to defend
#if possible, barracks will produce a soldier in an adjacent space
#Soldiers will move one square randomly *if not near enemy soldiers* and if possible to move
#soldiers will attack a random enemy adjacent (not diagonal) and if no enemies around, attacks a random building, if not buildings, moves towards enemy capital

import os
import colorama
from colorama import Fore

#Set Grid
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
Grid = [[(Fore.WHITE + ". ") for x in range(GridSize)] for x in range(GridSize)]

################### How the grid works ###################

# Grid is a list of lists (like all grids)
# 0 means empty
# 1 means barracks
# 2 means farm
# 3 means soldier on 1 hp
# 4-10 means soldier on x-2 hp (max of 8 hp)
# Blue and Red are team colors, White for empty tiles

################### How the grid works ###################

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

Print()