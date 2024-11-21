'''
ID: ethanfung8
LANG: PYTHON3
PROG: replace
'''

HOME_FILES = True
OUTPUT_TO_FILES = False

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/replace/replace.in", "r")
else:
  File = open(r"replace.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace() or Input[-1] == "":
  Input = Input[:-1]
  
#################################################################################################



"""
CODE HERE!!!!

find/replace instances of 'replace' 
with the name of the program

Also, change the chapter number if neccesary
"""



#################################################################################################

if OUTPUT_TO_FILES:
  if HOME_FILES:
    File = open(r"USACO/Practice/Chapter 1/replace/replace.out", "x")
  else:
    File = open(r"replace.out", "x")
  File.write(Out)
  File.close()