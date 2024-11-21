Input = "212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164"

# Input = "1,2,4"

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
print(String)
