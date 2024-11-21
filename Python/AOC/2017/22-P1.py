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

Infected = []

for Row in range(SquareSize):
  for Column in range(SquareSize):
    if Input[Row][Column] == "#":
      Infected.append([Row - Offset, Column - Offset])

print(Infected)

Output = 0
for Burst in range(1, 10001):
  if (Burst % 1000 == 0):
    print(Burst)
  if [VirusRow, VirusColumn] in Infected:
    #Turn Right!
    VirusDirection = ["Up", "Right", "Down", "Left"][["Left", "Up", "Right", "Down"].index(VirusDirection)]
  else:
    #Turn left!
    VirusDirection = ["Left", "Up", "Right", "Down"][["Up", "Right", "Down", "Left"].index(VirusDirection)]
    
  if [VirusRow, VirusColumn] in Infected:
    Infected.remove([VirusRow, VirusColumn])
    # print(Infected)
  else:
    Infected.append([VirusRow, VirusColumn])
    Output += 1
    # print(Infected)
    
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