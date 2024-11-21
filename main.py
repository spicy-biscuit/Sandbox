import os
import importlib
import timeit

"""
Project Formatting:

if not in a file:
'ProjectName'

if in a file:
'File1.File2.File3.ProjectName'
"""
AOCProject = "AOC.2022.16-P2"
USACOProject = "USACO.Practice.Chapter 1.ariprog.ariprog"
DCPProject = "DCP.1-20.5"
CodeForcesProject = "CodeForces.1400.1285C"
EulerProject = "Euler.1-100.61-80.68"
RandomProject = "Random.Ropes"

#SHIFT THIS ONE!!!
#AOC, USACO, DCP, CF, Euler, Random
CurrentProject = "Euler"

if CurrentProject == "AOC":
  CurrentProject = AOCProject
if CurrentProject == "USACO":
  CurrentProject = USACOProject
if CurrentProject == "DCP":
  CurrentProject = DCPProject
if CurrentProject == "CF":
  CurrentProject = CodeForcesProject
if CurrentProject == "Euler":
  CurrentProject = EulerProject
if CurrentProject == "Random":
  CurrentProject = RandomProject
List = []

print("Available Programs: \nAOC\nUSACO\nDCP\nCodeForces\nRandom\n")

First = True
while True:
  if First == False:
    os.system("clear")
  First = False
  print("Which program would you like to run?")
  Input = input()
  Start = timeit.default_timer()
  if Input == "":
    Input = CurrentProject
  #Game of Life exception:
  if Input.lower() == "game of life":
    Input = "GameOfLife"
  if Input in List:
    importlib.reload(__import__(Input))
  else:
    __import__(Input)
  List.append(Input)
  End = timeit.default_timer()
  #TIME
  TOTAL_SECONDS = End-Start
  if TOTAL_SECONDS < 20:
    TOTAL_SECONDS = round(TOTAL_SECONDS, 5)
  else:
    TOTAL_SECONDS = round(TOTAL_SECONDS, 2)
  TOTAL_MINUTES = int((TOTAL_SECONDS-TOTAL_SECONDS%60)/60)
  TOTAL_SECONDS = TOTAL_SECONDS%60
  TOTAL_HOURS = int((TOTAL_MINUTES-TOTAL_MINUTES%60)/60)
  TOTAL_MINUTES = TOTAL_MINUTES%60
  
#################################################
#################################################

  String = ""
  if TOTAL_SECONDS < 20:
    TOTAL_SECONDS = round(TOTAL_SECONDS, 5)
  else:
    TOTAL_SECONDS = round(TOTAL_SECONDS, 2)
  if TOTAL_MINUTES == 0 and TOTAL_HOURS == 0:
    Length = len("Total time taken: " + str(TOTAL_SECONDS) + " seconds.")
  elif TOTAL_HOURS == 0:
    Length = len("Total time taken: " + str(TOTAL_MINUTES) + " minutes and " + str(TOTAL_SECONDS) + " seconds.")
  else:
    Length = len("Total time taken: " + str(TOTAL_HOURS) + "hours, " + str(TOTAL_MINUTES) + " minutes and " + str(TOTAL_SECONDS) + " seconds.")

  for x in range(Length+5):
    String = String + "-"
  
#################################################
#################################################
  
  print()
  print(String)
  print("Program End\n")
  if TOTAL_SECONDS < 20:
    TOTAL_SECONDS = round(TOTAL_SECONDS, 5)
  else:
    TOTAL_SECONDS = round(TOTAL_SECONDS, 2)
  if TOTAL_MINUTES == 0 and TOTAL_HOURS == 0:
    print("Total time taken: " + str(TOTAL_SECONDS) + " seconds.")
  elif TOTAL_HOURS == 0:
    print("Total time taken: " + str(TOTAL_MINUTES) + " minutes and " + str(TOTAL_SECONDS) + " seconds.")
  else:
    print("Total time taken: " + str(TOTAL_HOURS) + "hours, " + str(TOTAL_MINUTES) + " minutes and " + str(TOTAL_SECONDS) + " seconds.")
  print(String)
  print()
  
#################################################
#################################################
  
  #Restting
  #Optional forced out:
  break
  #Choose
  RESET_INPUT = input("Would you like to run another program?")
  RESET_INPUT.lower()
  if RESET_INPUT == "n" or RESET_INPUT == "no":
    break