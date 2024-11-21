PuzzleInput = "ugkiagan"
# PuzzleInput = "flqrgnkx"

from functools import cache

@cache
def KnotHash(Input):
  List = [x for x in range(256)]
  
  RealInput = []
  
  for x in range(len(Input)):
    RealInput.append(ord(Input[x]))
  
  Input = RealInput
  Input = Input + [17, 31, 73, 47, 23]
  
  
  def Function(List, CurrentPosition, SkipSize, Length):
    while True:
      if CurrentPosition >= len(List):
        CurrentPosition -= len(List)
      else:
        break
    Subset = []
    OriginalPosition = CurrentPosition
    for x in range(Length):
      if CurrentPosition + x >= len(List):
        CurrentPosition -= len(List)
      Subset.append(List[CurrentPosition + x])
    Subset.reverse()
    CurrentPosition = OriginalPosition
    # print(List)
    for x in range(Length):
      if CurrentPosition + x >= len(List):
        CurrentPosition -= len(List)
      List[CurrentPosition + x] = Subset[x]
    
    CurrentPosition = OriginalPosition
    CurrentPosition += Length + SkipSize
    while True:
      if CurrentPosition >= len(List):
        CurrentPosition -= len(List)
      else:
        break
    return(CurrentPosition)
  
  CurrentPosition = 0
  SkipSize = 0
  for x in range(64):
    for Length in Input:
      CurrentPosition = Function(List, CurrentPosition, SkipSize, Length)
      # print(List, CurrentPosition)
      SkipSize += 1
  
  # print(List)
  
  NewList = []
  for x in range(16):
    Item = List[16 * x]
    for y in range(1, 16):
      Item = Item ^ List[16 * x + y]
    NewList.append(Item)
  # print(NewList)
  
  String = ""
  for x in NewList:
    Item = str(hex(x))
    if len(Item) == 3:
      Item = Item[:2] + "0" + Item[2]
    # print(Item)
    String = String + Item[2:]
  return(String)

@cache
def IncrementBinary(String):
  if String == "":
    return("1")
  if String[-1] == "0":
    return(String[:-1] + "1")
  return(IncrementBinary(String[:-1]) + "0")

@cache
def ReturnBinary(Character):
  if Character == "0":
    return("0000")
  if Character == "a":
    return("1010")
  return(IncrementBinary(ReturnBinary(chr(ord(Character) - 1))))

Total = 0
for x in range(128):
  HashInput = PuzzleInput + "-" + str(x)
  HashOutput = KnotHash(HashInput)
  String = ""
  for x in range(len(HashOutput)):
    x = HashOutput[x]
    x = ReturnBinary(x)
    String = String + x
  print(String)
  for x in range(len(String)):
    if String[x] == "1":
      Total += 1

print(Total)