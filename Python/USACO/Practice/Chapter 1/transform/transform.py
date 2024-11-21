'''
ID: ethanfung8
LANG: PYTHON3
PROG: transform
'''

# File = open(r"USACO/Practice/Chapter 1/transform/transform.in", "r")
File = open(r"transform.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

N = int(Input[0])
Input = Input[1:]

Original = Input[:N]
New = Input[N:]

OriginalGrid = [["-" for x in range(N)] for x in range(N)]
NewGrid = [["-" for x in range(N)] for x in range(N)]

for Row in range(N):
  for Column in range(N):
    OriginalGrid[Row][Column] = Original[Row][Column]
    NewGrid[Row][Column] = New[Row][Column]

def Rotate(Grid, Repeats):
  ThisNew = [["-" for x in range(N)] for x in range(N)]
  for Row in range(N):
    for Column in range(N):
      ThisNew[Row][Column] = Grid[N - Column - 1][Row]
  if Repeats == 1:
    return(ThisNew)
  return(Rotate(ThisNew, Repeats - 1))

def Reflection(Grid):
  Length = N - 1
  ThisNew = [["-" for x in range(N)] for x in range(N)]
  for Row in range(N):
    for Column in range(N):
      ThisNew[Row][Column] = Grid[Row][Length - Column]
  return(ThisNew)

def IsEqual(Grid1, Grid2):
  Out = True
  for Row in range(N):
    for Column in range(N):
      if Grid1[Row][Column] != Grid2[Row][Column]:
        Out = False
        break
  return(Out)

Out = 0
if IsEqual(Rotate(Original, 1), New):
  Out = 1
elif IsEqual(Rotate(Original, 2), New):
  Out = 2
elif IsEqual(Rotate(Original, 3), New):
  Out = 3
elif IsEqual(Reflection(Original), New):
  Out = 4
elif IsEqual(Reflection(Rotate(Original, 1)), New) or IsEqual(Reflection(Rotate(Original, 2)), New) or IsEqual(Reflection(Rotate(Original, 3)), New):
  Out = 5
elif IsEqual(Original, New):
  Out = 6
else:
  Out = 7

print(Out)

# File = open(r"USACO/Practice/Chapter 1/transform/transform.out", "x")
File = open(r"transform.out", "x")
File.write(str(Out) + "\n")
File.close()