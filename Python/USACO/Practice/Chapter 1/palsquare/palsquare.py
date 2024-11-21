'''
ID: ethanfung8
LANG: PYTHON3
PROG: palsquare
'''

# File = open(r"USACO/Practice/Chapter 1/palsquare/palsquare.in", "r")
File = open(r"palsquare.in", "r")
Input = File.read()
File.close()

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

Base = int(Input)
Out = ""
for x in range(1, 301):
  Squared = x ** 2
  Squared = ConvertBase(Squared, Base)
  if IsPalindrome(Squared):
    Out = Out + ConvertBase(x, Base) + " " + Squared + "\n"

# File = open(r"USACO/Practice/Chapter 1/palsquare/palsquare.out", "x")
File = open(r"palsquare.out", "x")
File.write(Out)
File.close()