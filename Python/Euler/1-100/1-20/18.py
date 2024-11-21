"""
18: Maximum Path Sum I
"""

Triangle = ["""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""]

def SplitGrid(Grid):
  #Split the lines
  Grid = Grid[0].split("\n")

  #Takes a string and makes a list of ints
  def Func(String):
    String = String.split()
    String = list(map(int, String))
    return(String)

  #Applies func to every line in grid
  Grid = list(map(Func, Grid))
  return(Grid)

Triangle = SplitGrid(Triangle)

# for x in (Triangle):
#   print(x)

while True:
  # print()
  # for x in Triangle:
  #   print(x)
  if len(Triangle) == 1:
    break
  TopLine = Triangle[-2]
  BottomLine = Triangle[-1]

  Length = len(TopLine)

  for Index in range(Length):
    TopLine[Index] += max(BottomLine[Index], BottomLine[Index + 1])
  Triangle = Triangle[:-1]

print(Triangle[0][0])
  