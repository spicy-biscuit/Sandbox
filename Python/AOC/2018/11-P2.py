Input = 7347
# Input = 42 #21,61
# Input = 18 #33,45

SerialID = Input

from functools import cache

@cache
def FindPowerLevel(X, Y, Serial):
  RackID = X + 10
  Out = RackID * Y
  Out += Serial
  Out *= RackID
  if Out < 100:
    Out = 0
  else:
    # print(Out, int(str(Out)[-3]))
    Out = int(str(Out)[-3])
  Out -= 5
  return(Out)

# print(FindPowerLevel(122, 79, 57))
# print(FindPowerLevel(217, 196, 39))
# print(FindPowerLevel(101, 153, 71))

@cache
def FindTotal(X, Y, Serial, GridSize):
  Out = 0
  if GridSize == 0:
    return(FindPowerLevel(X, Y, Serial))
  if GridSize % 2 == 0:
    Out = 0
    Out += FindTotal(X, Y, Serial, int(GridSize / 2))
    Out += FindTotal(X + int(GridSize/2), Y, Serial, int(GridSize / 2))
    Out += FindTotal(X, Y + int(GridSize/2), Serial, int(GridSize / 2))
    Out += FindTotal(X + int(GridSize/2), Y + int(GridSize/2), Serial, int(GridSize / 2))
    return(Out)
  if GridSize % 3 == 0:
    Out = 0
    Adder = int(GridSize / 3)
    for a in range(3):
      for b in range(3):
        Out += FindTotal(X + a * Adder, Y + b * Adder, Serial, Adder)
    return(Out)
  if GridSize % 5 == 0:
    Out = 0
    Adder = int(GridSize / 5)
    for a in range(5):
      for b in range(5):
        Out += FindTotal(X + a * Adder, Y + b * Adder, Serial, Adder)
    return(Out)
  if GridSize % 7 == 0:
    Out = 0
    Adder = int(GridSize / 7)
    for a in range(7):
      for b in range(7):
        Out += FindTotal(X + a * Adder, Y + b * Adder, Serial, Adder)
    return(Out)
  
  Out = FindTotal(X, Y, Serial, GridSize - 1)
  for x in range(GridSize - 1):
    # print(X + GridSize - 1, Y + x)
    # print(X + x, Y + GridSize - 1)
    Out += FindPowerLevel(X + GridSize - 1, Y + x, Serial)
    Out += FindPowerLevel(X + x, Y + GridSize - 1, Serial)
  # print(X + GridSize - 1, Y + GridSize - 1)
  Out += FindPowerLevel(X + GridSize - 1, Y + GridSize - 1, Serial)
  return(Out)

Max = 0
Out = (0, 0)
MaxNumSize = 0
for GridSize in range(1, 301):
  print(GridSize)
  for X in range(1, 302 - GridSize):
    for Y in range(1, 302 - GridSize):
      Val = FindTotal(X, Y, SerialID, GridSize)
      if Val > Max:
        Max = Val
        Out = (X, Y)
        MaxNumSize = GridSize
        # print(Out, GridSize, Max)

print(str(Out[0]) + "," + str(Out[1]) + "," + str(MaxNumSize), Max)