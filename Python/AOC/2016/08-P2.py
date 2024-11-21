Input = ["""rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=0 by 10
rotate column x=5 by 2
rotate column x=0 by 1
rect 9x1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=40 by 1
rotate column x=27 by 1
rotate column x=22 by 1
rotate column x=17 by 1
rotate column x=12 by 1
rotate column x=7 by 1
rotate column x=2 by 1
rotate row y=2 by 5
rotate row y=1 by 3
rotate row y=0 by 5
rect 1x3
rotate row y=2 by 10
rotate row y=1 by 7
rotate row y=0 by 2
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 5
rotate row y=1 by 3
rotate row y=0 by 3
rect 1x3
rotate column x=45 by 1
rotate row y=2 by 7
rotate row y=1 by 10
rotate row y=0 by 2
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 13
rotate row y=0 by 5
rotate column x=3 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=0 by 5
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 8
rotate row y=0 by 5
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 17
rotate row y=2 by 20
rotate row y=0 by 15
rotate column x=13 by 1
rotate column x=12 by 3
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=0 by 1
rect 14x1
rotate row y=1 by 47
rotate column x=9 by 1
rotate column x=4 by 1
rotate row y=3 by 3
rotate row y=2 by 10
rotate row y=1 by 8
rotate row y=0 by 5
rotate column x=2 by 2
rotate column x=0 by 2
rect 3x2
rotate row y=3 by 12
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=8 by 1
rotate column x=7 by 3
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=0 by 20
rotate column x=46 by 1
rotate row y=4 by 17
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=1 by 5
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=32 by 4
rotate row y=4 by 33
rotate row y=3 by 5
rotate row y=2 by 15
rotate row y=0 by 15
rotate column x=13 by 1
rotate column x=12 by 3
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=39 by 3
rotate column x=35 by 4
rotate column x=20 by 4
rotate column x=19 by 3
rotate column x=10 by 4
rotate column x=9 by 3
rotate column x=8 by 3
rotate column x=5 by 4
rotate column x=4 by 3
rotate row y=5 by 5
rotate row y=4 by 5
rotate row y=3 by 33
rotate row y=1 by 30
rotate column x=48 by 1
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=38 by 3
rotate column x=37 by 3
rotate column x=36 by 5
rotate column x=35 by 1
rotate column x=33 by 1
rotate column x=32 by 5
rotate column x=31 by 5
rotate column x=30 by 1
rotate column x=23 by 4
rotate column x=22 by 3
rotate column x=21 by 3
rotate column x=20 by 1
rotate column x=12 by 2
rotate column x=11 by 2
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 3
rotate column x=0 by 4"""]

# Input = ["""rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1"""] #fake

Input = Input[0].split("\n")

Grid = [["." for x in range(50)] for y in range(6)]
# Grid = [["." for x in range(7)] for y in range(3)] #fake

def Rectangle(A, B):
  for Column in range(A):
    for Row in range(B):
      Grid[Row][Column] = "#"

def RotateRow(Row, Number):
  for x in range(Number):
    Grid[Row] = [Grid[Row][-1]] + Grid[Row][:-1]

def RotateColumn(Column, Number):
  for x in range(Number):
    List = ["." for x in range(6)] #change back to 6
    for y in range(6): #change back to 6
      List[y] = (Grid[y][Column])
    # print(List)
    List = [List[-1]] + List[:-1]
    # print(List)
    for y in range(6): #change back to 6
      Grid[y][Column] = List[y]

for Instruction in Input:
  if Instruction[:4] == "rect":
    Instruction = Instruction[5:]
    Instruction = Instruction.split("x")
    A = int(Instruction[0])
    B = int(Instruction[1])
    Rectangle(A, B)
  elif Instruction.find("row") != -1:
    Row = int(Instruction[Instruction.find("=") + 1:Instruction.find("by") - 1])
    Number = int(Instruction[Instruction.find("by") + 3:])
    RotateRow(Row, Number)
  elif Instruction.find("column") != -1:
    Column = int(Instruction[Instruction.find("=") + 1:Instruction.find("by") - 1])
    Number = int(Instruction[Instruction.find("by") + 3:])
    RotateColumn(Column, Number)
  # for x in Grid:
  #   String = ""
  #   for y in x:
  #     String = String + y
  #   print(String)
  # print("---")

Total = 0
for x in Grid:
  for y in x:
    if y == "#":
      Total += 1
      
for x in Grid:
  String = ""
  for y in x:
    String = String + y
  print(String)
print("---")

print(Total)