'''
ID: ethanfung8
LANG: PYTHON3
PROG: ariprog
'''

HOME_FILES = True
OUTPUT_TO_FILES = False

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/ariprog/ariprog.in", "r")
else:
  File = open(r"ariprog.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace() or Input[-1] == "":
  Input = Input[:-1]
  
#################################################################################################

N = int(Input[0])
M = int(Input[1])

MaxValue = M ** 2 + M ** 2

IsBiSquare = [False for x in range(MaxValue + 10)]
AllBiSquares = []
SetAllBiSquares = set([])
for p in range(M + 1):
  for q in range(M + 1):
    a = p ** 2 + q ** 2
    IsBiSquare[a] = True
    if a not in SetAllBiSquares:
      AllBiSquares.append(a)
      SetAllBiSquares.add(a)
AllBiSquares.sort()

print()
print("Starting...")
print()

Out = []

for p in range(M + 1):
  for q in range(p, M + 1):
    #q >= p
    BiSquare = q ** 2 + p ** 2
    Differences = []
    

print()
print("Sorting...")
print()

def SortFunc(tuple):
  return(100000 * tuple[1] + tuple[0])
if len(Out) == 0:
  Out = "NONE\n"

else:
  Out.sort(key=SortFunc)
  This = ""
  for x in Out:
    This = This + str(x[0]) + " " + str(x[1]) + "\n"
  Out = This
  
print(Out)

#################################################################################################

if OUTPUT_TO_FILES:
  if HOME_FILES:
    File = open(r"USACO/Practice/Chapter 1/ariprog/ariprog.out", "x")
  else:
    File = open(r"ariprog.out", "x")
  File.write(Out)
  File.close()