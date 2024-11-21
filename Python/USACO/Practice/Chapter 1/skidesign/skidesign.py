'''
ID: ethanfung8
LANG: PYTHON3
PROG: skidesign
'''

HOME_FILES = False
OUTPUT_TO_FILES = True

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/skidesign/skidesign.in", "r")
else:
  File = open(r"skidesign.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace() or Input[-1] == "":
  Input = Input[:-1]
  
#################################################################################################

N = int(Input[0])
Elevations = Input[1:]

for x in range(len(Elevations)):
  Elevations[x] = int(Elevations[x])

print(Elevations)
Min = min(Elevations)
Max = max(Elevations)

Out = float('inf')
for NewSmallest in range(Min, Max):
  This = 0
  NewBiggest = NewSmallest + 17
  for x in Elevations:
    if x < NewSmallest:
      This += (NewSmallest - x) ** 2
    if x > NewBiggest:
      This += (x - NewBiggest) ** 2
  if This < Out:
    Out = This

Out = str(Out)
Out = Out + "\n"
print(Out)

#################################################################################################

if OUTPUT_TO_FILES:
  if HOME_FILES:
    File = open(r"USACO/Practice/Chapter 1/skidesign/skidesign.out", "x")
  else:
    File = open(r"skidesign.out", "x")
  File.write(Out)
  File.close()