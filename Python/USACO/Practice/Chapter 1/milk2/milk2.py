'''
ID: ethanfung8
LANG: PYTHON3
PROG: milk2
'''

import math

# File = open(r"USACO/Practice/Chapter 1/milk2/milk2.in", "r")
File = open(r"milk2.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

NumFarmers = Input[0]
Input = Input[1:]

def SortFunc(Tuple):
  return(100000*Tuple[0] + Tuple[1])

def Union(AllTuples):
  print(len(AllTuples))
  # if len(AllTuples) > 8:
  #   return(Union(Union(AllTuples[:len(AllTuples) // 2]) + Union(AllTuples[len(AllTuples) // 2:])))
  # print(AllTuples)
  if len(AllTuples) == 1:
    return([AllTuples[0]])

  #Check if first two are combinable
  First = AllTuples[0]
  Second = AllTuples[1]
  FStart = First[0]
  FEnd = First[1]
  SStart = Second[0]
  SEnd = Second[1]

  if SStart <= FEnd:
    New = (FStart, max(FEnd, SEnd))
    if len(AllTuples) == 2:
      return([New])
    return(Union([New] + AllTuples[2:]))

  #Apply Union to the rest if first two are not combinable
  return([First] + Union(AllTuples[1:]))

In = []

for x in Input:
  x = x.split()
  if x == []:
    continue
  x[0] = int(x[0])
  x[1] = int(x[1])
  In.append((x[0], x[1]))
  
def MergeSort(Input):
  if len(Input) == 1:
    return(Input)
  Length = len(Input)
  Length = math.ceil(Length/2)
  List1 = MergeSort(Input[:Length])
  List2 = MergeSort(Input[Length:])
  Input = []
  while List1 != [] and List2 != []:
    if List1[0][0] < List2[0][0]:
      Input.append(List1[0])
      List1 = List1[1:]
    else:
      Input.append(List2[0])
      List2 = List2[1:]
  return(Input + List1 + List2)

# print(In)

if len(In) > 1:
  In = MergeSort(In)

# print(In)

if len(In) > 500:
  In1 = In[:len(In) // 6]
  In2 = In[1 * len(In) // 6: 2 * len(In) // 6]
  In3 = In[2 * len(In) // 6: 3 * len(In) // 6]
  In4 = In[3 * len(In) // 6: 4 * len(In) // 6]
  In5 = In[4 * len(In) // 6: 5 * len(In) // 6]
  In6 = In[5 * len(In) // 6:]
  In1 = Union(In1)
  In2 = Union(In2)
  In3 = Union(In3)
  In4 = Union(In4)
  In5 = Union(In5)
  In6 = Union(In6)
  print(len(In1), len(In2), len(In3), len(In4), len(In5), len(In6))
  In = Union(In1 + In2)
  In = Union(In + In3)
  In = Union(In + In4)
  In = Union(In + In5)
  In = Union(In + In6)
  
Input = (Union(In))

MaxContinuous = 0
for x in Input:
  New = x[1] - x[0]
  if New > MaxContinuous:
    MaxContinuous = New
print(MaxContinuous)

MaxUnContinuous = 0
for x in range(len(Input) - 1):
  First = Input[x]
  Second = Input[x + 1]

  First = First[1]
  Second = Second[0]

  Distance = Second - First
  if Distance > MaxUnContinuous:
    MaxUnContinuous = Distance

print(MaxUnContinuous)
OutString = str(MaxContinuous) + " " + str(MaxUnContinuous)



# File = open(r"USACO/Practice/Chapter 1/milk2/milk2.out", "x")
File = open(r"milk2.out", "x")
File.write(OutString + "\n")
File.close()