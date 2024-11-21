'''
ID: ethanfung8
LANG: PYTHON3
PROG: dualpal
'''

# File = open(r"USACO/Practice/Chapter 1/dualpal/dualpal.in", "r")
File = open(r"dualpal.in", "r")
Input = File.read()
File.close()

Input = Input.split()
N = int(Input[0])
S = int(Input[1])

def ConvertBase(Number, Base):
  NumsNeeded = 0
  while True:
    NumsNeeded += 1
    if Base ** NumsNeeded > Number:
      break
  String = ""
  for x in range(NumsNeeded):
    BaseValue = Base ** (NumsNeeded - x - 1)
    InsertNumber = Number // BaseValue
    Number -= InsertNumber * BaseValue
    if InsertNumber > 9:
      InsertNumber = chr(InsertNumber + 55)
    String = String + str(InsertNumber)
  return(String)

def IsPalindrome(String):
  if String == String[::-1]:
    return(True)
  return(False)

def IsDualPal(Int):
  Count = 0
  for Base in range(2, 11):
    if IsPalindrome(ConvertBase(Int, Base)):
      Count += 1
  if Count >= 2:
    return(True)
  return(False)

List = []
This = S
while True:
  if len(List) == N:
    break
  This += 1
  if IsDualPal(This):
    List.append(This)

print(List)
Out = ""
for x in List:
  Out = Out + str(x) + "\n"

# File = open(r"USACO/Practice/Chapter 1/dualpal/dualpal.out", "x")
File = open(r"dualpal.out", "x")
File.write(Out)
File.close()