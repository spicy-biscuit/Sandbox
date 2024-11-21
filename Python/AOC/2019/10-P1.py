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
  for x in range(Iterations - 1):
    CurrentRow += RowAdder
    CurrentColumn += ColumnAdder
    if Input[CurrentRow][CurrentColumn] == "#":
      return(False)
  return(True)


Max = 0
for Location in AllAsteroids:
  # print("*", Location)
  Visible = 0
  for Asteroid in AllAsteroids:
    if Asteroid == Location:
      continue
    if Sight(Location, Asteroid):
      # print(Asteroid)
      Visible += 1
  # print(Visible)
  # print("----------")
  if Visible > Max:
    Max = Visible
print(Max)
