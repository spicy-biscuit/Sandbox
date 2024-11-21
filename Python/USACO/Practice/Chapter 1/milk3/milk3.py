'''
ID: ethanfung8
LANG: PYTHON3
PROG: milk3
'''

HOME_FILES = False
OUTPUT_TO_FILES = True

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/milk3/milk3.in", "r")
else:
  File = open(r"milk3.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace() or Input[-1] == "":
  Input = Input[:-1]
  
#################################################################################################

Input = Input[0].split()
MaxA = int(Input[0])
MaxB = int(Input[1])
MaxC = int(Input[2])
# print(MaxA, MaxB, MaxC)

def Pour(First, MaxSecond, Second):
  # print()
  # print(MaxSecond, First, Second)
  Second = Second + First
  First = 0
  if Second > MaxSecond:
    Difference = MaxSecond - Second
    Second = MaxSecond
    First = abs(Difference)
  # print(First, Second)
  return([First, Second])

Seen = set([])
def AllSolutions(A, B, C):
  if (A, B, C) in Seen:
    return(set([]))
  Seen.add((A, B, C))
  # if A == 0:
  #   return(set([C]))

  RealOut = set([])
  if A == 0:
    RealOut.add(C)
  #Pour A into B
  List = Pour(A, MaxB, B)
  NewA = List[0]
  NewB = List[1]
  for x in AllSolutions(NewA, NewB, C):
    RealOut.add(x)

  #Pour A into C
  List = Pour(A, MaxC, C)
  NewA = List[0]
  NewC = List[1]
  for x in AllSolutions(NewA, B, NewC):
    RealOut.add(x)

  #Pour B into A
  List = Pour(B, MaxA, A)
  NewB = List[0]
  NewA = List[1]
  for x in AllSolutions(NewA, NewB, C):
    RealOut.add(x)

  #Pour B into C
  List = Pour(B, MaxC, C)
  NewB = List[0]
  NewC = List[1]
  for x in AllSolutions(A, NewB, NewC):
    RealOut.add(x)

  #Pour C into A
  List = Pour(C, MaxA, A)
  NewC = List[0]
  NewA = List[1]
  for x in AllSolutions(NewA, B, NewC):
    RealOut.add(x)

  #Pour C into B
  List = Pour(C, MaxB, B)
  NewC = List[0]
  NewB = List[1]
  for x in AllSolutions(A, NewB, NewC):
    RealOut.add(x)
  # print(RealOut)
  return(RealOut)

Out = ""
List = list(AllSolutions(0, 0, MaxC))
List.sort()
for x in List:
  Out = Out + str(x) + " "
Out = Out[:-1] + "\n"
print(Out)

#################################################################################################

if OUTPUT_TO_FILES:
  if HOME_FILES:
    File = open(r"USACO/Practice/Chapter 1/milk3/milk3.out", "x")
  else:
    File = open(r"milk3.out", "x")
  File.write(Out)
  File.close()