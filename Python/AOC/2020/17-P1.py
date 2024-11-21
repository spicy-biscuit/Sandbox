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

Active = []
for Row in range(len(Input)):
  for Column in range(len(Input[0])):
    if Input[Row][Column] == "#":
      Active.append((Row, Column, 0))

print(Active)

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
  Out = 0
  for x in range(-1, 2):
    for y in range(-1, 2):
      for z in range(-1, 2):
        if (x, y, z) == (0, 0, 0):
          continue
        if (X + x, Y + y, Z + z) in Active:
          Out += 1
  return(Out)

for CYCLE in range(6):
  New = []
  MinZ = min(Active, key=FindZ)[2] - 1
  MaxZ = max(Active, key=FindZ)[2] + 2
  MinY = min(Active, key=FindY)[1] - 1
  MaxY = max(Active, key=FindY)[1] + 2
  MinX = min(Active, key=FindX)[0] - 1
  MaxX = max(Active, key=FindX)[0] + 2
  for Z in range(MinZ, MaxZ):
    for Y in range(MinY, MaxY):
      for X in range(MinX, MaxX):
        Neighbors = FindNeighbors((X, Y, Z))
        IsActive = (X, Y, Z) in Active
        if IsActive:
          if Neighbors in [2, 3]:
            New.append((X, Y, Z))
        else:
          if Neighbors == 3:
            New.append((X, Y, Z))
  Active = New
print(len(Active))