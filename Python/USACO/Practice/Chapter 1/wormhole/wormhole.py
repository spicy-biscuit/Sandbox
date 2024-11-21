'''
ID: ethanfung8
LANG: PYTHON3
PROG: wormhole
'''

HOME_FILES = False
OUTPUT_TO_FILES = True

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/wormhole/wormhole.in", "r")
else:
  File = open(r"wormhole.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace() or Input[-1] == "":
  Input = Input[:-1]
  
#################################################################################################

N = int(Input[0])

Input = Input[1:]

Wormholes = []
for x in Input:
  x = x.split()
  x[0] = int(x[0])
  x[1] = int(x[1])
  Wormholes.append((x[0], x[1]))

# print(Wormholes)

RowIndexes = []
Rows = []
for x in Wormholes:
  if x[1] in RowIndexes:
    Rows[RowIndexes.index(x[1])].append(x)
  else:
    RowIndexes.append(x[1])
    Rows.append([x])

Count = 64
for x in range(len(Rows)):
  y = Rows[x]
  for z in range(len(y)):
    Count += 1
    y[z] = chr(Count)

# for x in Rows:
#   print(x)

def AllWormholePairs(Remaining):
  if Remaining == 0:
    Remaining = [chr(x + 65) for x in range(N)]
  First = Remaining[0]

  if len(Remaining) == 2:
    return([(Remaining[0], Remaining[1])])

  List = []
  for x in Remaining[1:]:
    New = Remaining.copy()
    New = New[1:]
    New.remove(x)
    This = AllWormholePairs(New)
    for y in range(len(This)):
      NewList = [(First, x)]
      if type(This[y]) is tuple:
        This[y] = [This[y]]
      for z in This[y]:
        NewList.append(z)
      This[y] = NewList
    List = List + This
  return(List)

def NextItem(ListOfRows, WormholeConnections, Current):
  if Current == "OUT":
    return("OUT")
  Index = -1
  for x in ListOfRows:
    if Current in x:
      if Current == x[-1]:
        return("OUT")
      Index = x.index(Current)
      Index += 1
      Current = x[Index]

  for Pairing in WormholeConnections:
    if Pairing[0] == Current:
      return(Pairing[1])
    if Pairing[1] == Current:
      return(Pairing[0])
  print("ERROR")

def CanLoop(ListOfRows, WormholeConnections):
  
  for START in [chr(x) for x in range(65, 65 + N)]:
    Current = START
    while True:
      Current = NextItem(ListOfRows, WormholeConnections, Current)
      if Current == "OUT":
        break
      if Current == START:
        return(True)
  return(False)

Out = 0
for x in (AllWormholePairs(0)):
  Out += (CanLoop(Rows, x))
Out = str(Out) + "\n"
print(Out)
#################################################################################################

if OUTPUT_TO_FILES:
  if HOME_FILES:
    File = open(r"USACO/Practice/Chapter 1/wormhole/wormhole.out", "x")
  else:
    File = open(r"wormhole.out", "x")
  File.write(Out)
  File.close()