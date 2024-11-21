Input = 277678

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""

"""
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
"""


from functools import cache

import math

# @cache
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
      return(tuple(OriginalCoordinates))
  for x in range(SquareLength - 1):
    OriginalCoordinates[1] = OriginalCoordinates[1] - 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(tuple(OriginalCoordinates))
  for x in range(SquareLength - 1):
    OriginalCoordinates[0] = OriginalCoordinates[0] + 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(tuple(OriginalCoordinates))
  for x in range(SquareLength - 1):
    OriginalCoordinates[1] = OriginalCoordinates[1] + 1
    SpacesToMove -= 1
    if SpacesToMove == 0:
      return(tuple(OriginalCoordinates))

@cache
def FindNumber(Coordinates): #coordinates is a tuple
  Row = Coordinates[0]
  Column = Coordinates[1]
  CheckThis = [Row, Column]
  if CheckThis == [0,0]:
    return(1)
  SquareNumber = max(abs(Row), abs(Column))
  SquareLength = 2 * SquareNumber + 1
  OriginalSpot = [SquareNumber, SquareNumber]
  OriginalNumber = (SquareLength - 2) ** 2
  for x in range(SquareLength - 1):
    OriginalSpot[0] = OriginalSpot[0] - 1
    OriginalNumber += 1
    if OriginalSpot == CheckThis:
      return(OriginalNumber)
  for x in range(SquareLength - 1):
    OriginalSpot[1] = OriginalSpot[1] - 1
    OriginalNumber += 1
    if OriginalSpot == CheckThis:
      return(OriginalNumber)
  for x in range(SquareLength - 1):
    OriginalSpot[0] = OriginalSpot[0] + 1
    OriginalNumber += 1
    if OriginalSpot == CheckThis:
      return(OriginalNumber)
  for x in range(SquareLength - 1):
    OriginalSpot[1] = OriginalSpot[1] + 1
    OriginalNumber += 1
    if OriginalSpot == CheckThis:
      return(OriginalNumber)

@cache
def WriteNumber(Number):
  Coordinates = FindCoordinates(Number)
  Row = Coordinates[0]
  Column = Coordinates[1]
  if Number == 1:
    return(1)
  Total = 0
  for RowChange in range(-1, 2):
    for ColumnChange in range(-1, 2):
      if RowChange == 0 and ColumnChange == 0:
        continue
      NewCoordinates = [Row + RowChange, Column + ColumnChange]
      NewNumber = FindNumber(tuple(NewCoordinates))
      # print(Coordinates, NewCoordinates, NewNumber)
      if NewNumber >= Number:
        continue
      Total += WriteNumber(NewNumber)
  return(Total)


# Input = 1024
# Input = 23
# Input = 12
# Input = 1

Square = 0
while True:
  Square += 1
  WrittenData = WriteNumber(Square)
  # print(Square, WrittenData)
  if WrittenData > Input:
    print("hi", WrittenData)
    break

# print(FindCoordinates(1))
# print(FindCoordinates(2))
# print(FindCoordinates(3))
# print(FindCoordinates(1))
# print(FindCoordinates(2))
# print(FindCoordinates(3))
# print(FindCoordinates(3))
# print(FindCoordinates(3))

