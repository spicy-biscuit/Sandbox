Input = ["""...##.#.#.####...###.....
..#..##.#...#.##.##.#..#.
.#.#.#.###....#...###....
.#....#..####.....##.#..#
##.#.#.#.#..#..#.....###.
#...##....##.##.#.##.##..
.....###..###.###...#####
######.####..#.#......##.
#..###.####..####........
#..######.##....####...##
...#.##.#...#.#.#.#..##.#
####.###..#####.....####.
#.#.#....#.####...####...
##...#..##.##....#...#...
......##..##..#..#..####.
.##..##.##..####..##....#
.#..#..##.#..##..#...#...
#.#.##.....##..##.#####..
##.#.......#....#..###.#.
##...#...#....###..#.#.#.
#....##...#.#.#.##..#..##
#..#....#####.....#.##.#.
.#...#..#..###....###..#.
..##.###.#.#.....###.....
#.#.#.#.#.##.##...##.##.#"""]

# Input = ["""..#
# #..
# ..."""]

Input = Input[0].split("\n")

SquareSize = len(Input)
Offset = int((SquareSize - 1) / 2)

VirusRow = 0
VirusColumn = 0
VirusDirection = "Up"

Infected = set([])
Weakened = set([])
Flagged = set([])

for Row in range(SquareSize):
  for Column in range(SquareSize):
    if Input[Row][Column] == "#":
      Infected.add(tuple([Row - Offset, Column - Offset]))

# print(Infected)

Output = 0
for Burst in range(1, 10000001):
  if (Burst % 100000 == 0):
    print(Burst, len(Weakened) + len(Infected) + len(Flagged))

  #TURNING
  if (VirusRow, VirusColumn) in Infected:
    #Turn Right!
    VirusDirection = ["Up", "Right", "Down", "Left"][["Left", "Up", "Right", "Down"].index(VirusDirection)]
  elif (VirusRow, VirusColumn) in Flagged:
    if VirusDirection == "Up":
      VirusDirection = "Down"
    elif VirusDirection == "Down":
      VirusDirection = "Up"
    elif VirusDirection == "Left":
      VirusDirection = "Right"
    elif VirusDirection == "Right":
      VirusDirection = "Left"
  elif (VirusRow, VirusColumn) in Weakened:
    VirusDirection = VirusDirection
  else:
    #Turn left!
    VirusDirection = ["Left", "Up", "Right", "Down"][["Up", "Right", "Down", "Left"].index(VirusDirection)]
    
  if (VirusRow, VirusColumn) in Infected:
    Infected.remove((VirusRow, VirusColumn))
    Flagged.add((VirusRow, VirusColumn))
  elif (VirusRow, VirusColumn) in Weakened:
    Weakened.remove((VirusRow, VirusColumn))
    Infected.add((VirusRow, VirusColumn))
    Output += 1
  elif (VirusRow, VirusColumn) in Flagged:
    Flagged.remove((VirusRow, VirusColumn))
  else: #this is a clean node
    Weakened.add((VirusRow, VirusColumn))
    
  #Move!
  if VirusDirection == "Up":
    VirusRow -= 1
  elif VirusDirection == "Down":
    VirusRow += 1
  elif VirusDirection == "Left":
    VirusColumn -= 1
  elif VirusDirection == "Right":
    VirusColumn += 1

print(Output)