'''
ID: ethanfung8
LANG: PYTHON3
PROG: beads
'''

# File = open(r"USACO/Practice/Chapter 1/beads/beads.in", "r")
File = open(r"beads.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")
NumBeads = int(Input[0])
Beads = list(Input[1])
OriginalBeads = []
for x in Beads:
  OriginalBeads.append(x)

print(Beads)

Max = 0
for SplitIndex in range(NumBeads + 1):
  # print("-----")
  Beads = OriginalBeads.copy()
  #Split index of 2:
  # bb|wrw
  #| is the split

  Beads = Beads[SplitIndex:] + Beads[:SplitIndex]

  Left = Beads.copy()
  Right = Beads.copy()
  Left.reverse()

  LeftCount = 0
  RightCount = 0

  #LEFT!!!!
  Index = 0
  LeftColor = ""
  for x in Left:
    if x != "w":
      LeftColor = x
      break
  for x in Left:
    if x not in ["w", LeftColor]:
      break
    else:
      LeftCount += 1

  Left = Left[LeftCount:]
  Right = Left
  Right.reverse()

  # print(Right)

  #RIGHT!!!!
  Index = 0
  RightColor = ""
  for x in Right:
    if x != "w":
      RightColor = x
      break
  for x in Right:
    if x not in ["w", RightColor]:
      break
    else:
      RightCount += 1

  Total = LeftCount + RightCount
  if Total > Max:
    Max = Total
  # print(SplitIndex, Total)

# File = open(r"USACO/Practice/Chapter 1/beads/beads.out", "x")
File = open(r"beads.out", "x")
File.write(str(Max) + "\n")
File.close()