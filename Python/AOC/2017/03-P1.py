Input = 277678

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""


import math

def FindCoordinates(Number):
  if math.sqrt(Number) % 2 == 1:
    Root = int(math.sqrt(Number))
    Coordinates = [(Root - 1) / 2, (Root - 1) / 2]
    Coordinates[0] = int(Coordinates[0])
    Coordinates[1] = int(Coordinates[1])
    return(Coordinates)
  Root = int(math.floor(math.sqrt(Number)))
  if Root % 2 == 0:
    Root -= 1
  SquareLength = Root + 2
  SpacesToMove = Number - Root ** 2
  OriginalCoordinates = FindCoordinates((Root + 2) ** 2)
  for x in range(SquareLength - 1):
    OriginalCoordinates[0] = OriginalCoordinates[0] - 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(OriginalCoordinates)
  for x in range(SquareLength - 1):
    OriginalCoordinates[1] = OriginalCoordinates[1] - 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(OriginalCoordinates)
  for x in range(SquareLength - 1):
    OriginalCoordinates[0] = OriginalCoordinates[0] + 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(OriginalCoordinates)
  for x in range(SquareLength - 1):
    OriginalCoordinates[1] = OriginalCoordinates[1] + 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(OriginalCoordinates)
  
  return("no")

# Input = 1024
# Input = 23
# Input = 12
# Input = 1

Coordinates = (FindCoordinates(Input))
print(Coordinates)
Total = 0
for x in Coordinates:
  Total += abs(x)
print(Total)