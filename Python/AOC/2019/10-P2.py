Input = [""".............#..#.#......##........#..#
.#...##....#........##.#......#......#.
..#.#.#...#...#...##.#...#.............
.....##.................#.....##..#.#.#
......##...#.##......#..#.......#......
......#.....#....#.#..#..##....#.......
...................##.#..#.....#.....#.
#.....#.##.....#...##....#####....#.#..
..#.#..........#..##.......#.#...#....#
...#.#..#...#......#..........###.#....
##..##...#.#.......##....#.#..#...##...
..........#.#....#.#.#......#.....#....
....#.........#..#..##..#.##........#..
........#......###..............#.#....
...##.#...#.#.#......#........#........
......##.#.....#.#.....#..#.....#.#....
..#....#.###..#...##.#..##............#
...##..#...#.##.#.#....#.#.....#...#..#
......#............#.##..#..#....##....
.#.#.......#..#...###...........#.#.##.
........##........#.#...#.#......##....
.#.#........#......#..........#....#...
...............#...#........##..#.#....
.#......#....#.......#..#......#.......
.....#...#.#...#...#..###......#.##....
.#...#..##................##.#.........
..###...#.......#.##.#....#....#....#.#
...#..#.......###.............##.#.....
#..##....###.......##........#..#...#.#
.#......#...#...#.##......#..#.........
#...#.....#......#..##.............#...
...###.........###.###.#.....###.#.#...
#......#......#.#..#....#..#.....##.#..
.##....#.....#...#.##..#.#..##.......#.
..#........#.......##.##....#......#...
##............#....#.#.....#...........
........###.............##...#........#
#.........#.....#..##.#.#.#..#....#....
..............##.#.#.#...........#....."""]

# Input = [""".#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##"""]

Input = Input[0].split("\n")

for x in range(len(Input)):
  Input[x] = list(Input[x])

import math
from functools import cache

@cache
def divisors(n):
  n = abs(n)
  large_divisors = []
  for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
      large_divisors.append(i)
      if i*i != n:
        large_divisors.append(int(n / i))
  large_divisors = list(set(large_divisors))
  large_divisors.sort()
  return(large_divisors)


AllAsteroids = []
for Row in range(len(Input)):
  for Column in range(len(Input[0])):
    if Input[Row][Column] == "#":
      AllAsteroids.append((Row, Column))

# print(AllAsteroids)

def Sight(Start, Finish):
  RowDifference = Finish[0] - Start[0]
  ColumnDifference = Finish[1] - Start[1]

  Iterations = 0
  RowDivisors = divisors(RowDifference)
  ColumnDivisors = divisors(ColumnDifference)

  for x in RowDivisors:
    if x in ColumnDivisors:
      if x > Iterations:
        Iterations = x

  RowAdder = 0
  ColumnAdder = 0
  if Iterations == 0:
    if RowDifference == 0:
      Iterations = abs(ColumnDifference)
    elif ColumnDifference == 0:
      Iterations = abs(RowDifference)
      
  ColumnAdder = int(ColumnDifference / Iterations)
  RowAdder = int(RowDifference / Iterations)

  CurrentRow = Start[0]
  CurrentColumn = Start[1]
  Out = 0
  for x in range(Iterations - 1):
    CurrentRow += RowAdder
    CurrentColumn += ColumnAdder
    if Input[CurrentRow][CurrentColumn] == "#":
      Out += 1
  return(Out)


Max = 0
Out = (0, 0)
for Location in AllAsteroids:
  # print("*", Location)
  Visible = 0
  for Asteroid in AllAsteroids:
    if Asteroid == Location:
      continue
    if Sight(Location, Asteroid) == 0:
      # print(Asteroid)
      Visible += 1
  # print(Visible)
  # print("----------")
  if Visible > Max:
    Max = Visible
    Out = Location

# print(Out)
AllAsteroids.remove(Out)

def SortFunction(Asteroid):
  InTheWay = 0

  #If asteroid is ABOVE observatory, RowDifference is NEGATIVE
  #If asteroid is BELOW observatory, RowDifference is POSITIVE
  RowDifference = Asteroid[0] - Out[0]
  #If asteroid is RIGHT of observatory, ColumnDifference is POSITIVE
  #If asteroid is LEFT of observatory, ColumnDifference is NEGATIVE
  ColumnDifference = Asteroid[1] - Out[1]

  Direction = -1
  if ColumnDifference == 0 and RowDifference < 0:
    Direction = 1
  elif ColumnDifference > 0 and RowDifference < 0:
    Direction = 2
  elif ColumnDifference > 0 and RowDifference == 0:
    Direction = 3
  elif ColumnDifference > 0 and RowDifference > 0:
    Direction = 4
  elif ColumnDifference == 0 and RowDifference > 0:
    Direction = 5
  elif ColumnDifference < 0 and RowDifference > 0:
    Direction = 6
  elif ColumnDifference < 0 and RowDifference == 0:
    Direction = 7
  elif ColumnDifference < 0 and RowDifference < 0:
    Direction = 8

  if Direction == -1:
    print('wtf')
    return('wtf')

  if ColumnDifference == 0:
    Slope = 100
  else:
    Slope = -1 * RowDifference / ColumnDifference

  # if Direction in [6, 8]:
  #   Slope *= -1

  InTheWay = Sight(Out, Asteroid)
  # print(Slope)
  return(-1 * Slope + 1000 * Direction + 100000000 * InTheWay)

print(Out)
AllAsteroids.sort(key=SortFunction)
# print(AllAsteroids)

Out = (AllAsteroids[200 - 1])
Out = (Out[1], Out[0])

print(Out[0] * 100 + Out[1])
