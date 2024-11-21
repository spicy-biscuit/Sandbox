Input = [212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164]

# Input = [3, 4, 1, 5]

List = [x for x in range(256)]
# List = [0, 1, 2, 3, 4]

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
for Length in Input:
  CurrentPosition = Function(List, CurrentPosition, SkipSize, Length)
  print(List, CurrentPosition)
  SkipSize += 1
print(List)
print("answer: " + str(List[0] * List[1]))
    