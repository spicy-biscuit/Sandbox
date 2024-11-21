Current = "#........#.#.#...###..###..###.#..#....###.###.#.#...####..##..##.#####..##...#.#.....#...###.#.####"

Input = ["""#..## => .
##..# => #
..##. => .
.##.# => #
..... => .
..### => #
###.# => #
#.... => .
#.##. => #
.#.## => #
#...# => .
...## => .
###.. => #
.#..# => .
####. => .
....# => .
##### => #
.###. => .
#..#. => .
##... => #
.#... => #
#.#.# => .
..#.. => #
...#. => #
##.#. => .
.##.. => #
.#.#. => .
#.#.. => .
..#.# => #
#.### => .
##.## => .
.#### => #"""]

# Current = "#..#.#..##......###...###"
# Input = ["""...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #"""]

Input = Input[0].split("\n")

Conditions = []
Outcomes = []

FirstIndex = 0
LastIndex = len(Current) - 1

for x in Input:
  Conditions.append(x[:5])
  Outcomes.append(x[9])

def Ensure(String):
  Out = [0, 0]
  while True:
    if String[:5] != ".....":
      String = "." + String
      Out[0] += 1
      continue
    break
  while True:
    if String[-5:] != ".....":
      String = String + "."
      Out[1] += 1
      continue
    break
  return([String] + Out)

def Update(String):
  if String not in Conditions:
    return(".")
  Index = Conditions.index(String)
  return(Outcomes[Index])

for Generation in range(20):
  FunctionOut = Ensure(Current)
  Current = FunctionOut[0]
  FirstIndex -= FunctionOut[1]
  LastIndex += FunctionOut[2]

  NewCurrent = ".."
  for x in range(2, len(Current) - 4):
    NewCurrent = NewCurrent + Update(Current[x-2:x+3])
  NewCurrent = NewCurrent + ".."
  Current = NewCurrent
  # print(NewCurrent)

ThisIndex = FirstIndex
Total = 0
for x in range(len(Current)):
  if Current[x] == "#":
    Total += ThisIndex
  ThisIndex += 1

print(Total)