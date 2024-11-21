'''
ID: ethanfung8
LANG: PYTHON3
PROG: barn1
'''

# File = open(r"USACO/Practice/Chapter 1/barn1/barn1.in", "r")
File = open(r"barn1.in", "r")
Input = File.read()
File.close()

if Input[-1].isspace():
  Input = Input[:-1]

Input = Input.split("\n")

Nums = Input[0]
Input = Input[1:]

Nums = Nums.split()
M = int(Nums[0])
S = int(Nums[1])
C = int(Nums[2])

FilledStalls = Input

for x in range(len(FilledStalls)):
  FilledStalls[x] = int(FilledStalls[x])

# FilledStalls = set(FilledStalls)

print(FilledStalls)

Current = "Stall"
CurrentLength = 0
Filled = []
Gaps = []
for x in range(min(FilledStalls), max(FilledStalls) + 1):
  if Current == "Stall":
    if x in FilledStalls:
      CurrentLength += 1
      continue
    else:
      Filled.append(CurrentLength)
      CurrentLength = 1
      Current = "Empty"
      continue
  else:
    if x not in FilledStalls:
      CurrentLength += 1
      continue
    else:
      Gaps.append(CurrentLength)
      CurrentLength = 1
      Current = "Stall"
Filled.append(CurrentLength)

print(Filled)
print(Gaps)

CurrentBoards = len(Filled)

Out = sum(Filled)
for x in range(CurrentBoards - M):
  Out += min(Gaps)
  Gaps.remove(min(Gaps))
print(Out)

Out = str(Out) + "\n"

# File = open(r"USACO/Practice/Chapter 1/barn1/barn1.out", "x")
File = open(r"barn1.out", "x")
File.write(Out)
File.close()