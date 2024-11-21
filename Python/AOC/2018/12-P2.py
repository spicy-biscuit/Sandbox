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

def Shorten(String, First):
  while True:
    if String[0] == ".":
      String = String[1:]
      First -= 1
      continue
    break
  while True:
    if String[-1] == ".":
      String = String[:-1]
      continue
    break
  return((String, First))

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

def Function(String, First):
  ThisIndex = First
  Total = 0
  for x in range(len(String)):
    if String[x] == "#":
      Total += ThisIndex
    ThisIndex += 1
  
  return(Total)

def Update(String):
  if String not in Conditions:
    return(".")
  Index = Conditions.index(String)
  return(Outcomes[Index])

Set = []
for Generation in range(1, 1001):
  print(Generation, len(Current), Function(Current, FirstIndex) - 80 * Generation)
  if (Shorten(Current, FirstIndex)) in Set:
    print(Generation, Set.index(Shorten(Current, FirstIndex)))
    break
  Set.append(Shorten(Current, FirstIndex))
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

print(Function(Current, FirstIndex))

print(80 * 50000000000 + 786 + 80)