Input = ["""......##
####.#..
.##....#
.##.#..#
........
.#.#.###
#.##....
####.#.."""]

# Input = [""".#.
# ..#
# ###"""]

Input = Input[0].split("\n")

Active = set([])
for Row in range(len(Input)):
  for Column in range(len(Input[0])):
    if Input[Row][Column] == "#":
      Active.add((Row, Column, 0, 0))

print(Active)

def FindW(Tuple):
  return(Tuple[3])

def FindZ(Tuple):
  return(Tuple[2])

def FindY(Tuple):
  return(Tuple[1])

def FindX(Tuple):
  return(Tuple[0])

def FindNeighbors(Tuple):
  X = Tuple[0]
  Y = Tuple[1]
  Z = Tuple[2]
  W = Tuple[3]
  Out = 0
  for x in range(-1, 2):
    for y in range(-1, 2):
      for z in range(-1, 2):
        for w in range(-1, 2):
          if (x, y, z, w) == (0, 0, 0, 0):
            continue
          if (X + x, Y + y, Z + z, W + w) in Active:
            Out += 1
  return(Out)

for CYCLE in range(6):
  print(CYCLE + 1)
  New = set([])
  MinZ = min(Active, key=FindZ)[2] - 1
  MaxZ = max(Active, key=FindZ)[2] + 2
  MinY = min(Active, key=FindY)[1] - 1
  MaxY = max(Active, key=FindY)[1] + 2
  MinX = min(Active, key=FindX)[0] - 1
  MaxX = max(Active, key=FindX)[0] + 2
  MinW = min(Active, key=FindW)[3] - 1
  MaxW = max(Active, key=FindW)[3] + 2
  for Z in range(MinZ, MaxZ):
    for Y in range(MinY, MaxY):
      for X in range(MinX, MaxX):
        for W in range(MinW, MaxW):
          Neighbors = FindNeighbors((X, Y, Z, W))
          IsActive = (X, Y, Z, W) in Active
          if IsActive:
            if Neighbors in [2, 3]:
              New.add((X, Y, Z, W))
          else:
            if Neighbors == 3:
              New.add((X, Y, Z, W))
  Active = New
print(len(Active))