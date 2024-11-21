Input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

# Input = "R2, L3"
# Input = "R8, R4, R4, R8"

Directions = ["N", "E", "S", "W"]

Visited = []

Direction = 0
Coordinates = [0, 0]

Instructions = Input.split(", ")

for Instruction in Instructions:
  if Instruction[0] == "R":
    Direction += 1
    if Direction == 4:
      Direction = 0
  if Instruction[0] == "L":
    Direction -= 1
    if Direction == -1:
      Direction = 3
  CurrDir = Directions[Direction]
  # print(CurrDir, Instruction[0])
  CurrDis = int(Instruction[1:])
  Breakout = False
  for x in range(CurrDis):
    if Coordinates not in Visited:
      X = Coordinates[0]
      Y = Coordinates[1]
      Visited.append([X, Y])
    else:
      Breakout = True
      # print(Visited, Coordinates)
      break
    if CurrDir == "N":
      Coordinates[0] = Coordinates[0] - 1
    if CurrDir == "S":
      Coordinates[0] = Coordinates[0] + 1
    if CurrDir == "W":
      Coordinates[1] = Coordinates[1] - 1
    if CurrDir == "E":
      Coordinates[1] = Coordinates[1] + 1
  if Breakout:
    break
  # print(Coordinates)

print(abs(Coordinates[0]) + abs(Coordinates[1]))