'''
ID: ethanfung8
LANG: PYTHON3
PROG: crypt1
'''

HOME_FILES = False

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/crypt1/crypt1.in", "r")
else:
  File = open(r"crypt1.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace():
  Input = Input[:-1]
  
#################################################################################################

Numbers = int(Input[0])
Input = Input[1:]

NumSet = Input[0].split()

for x in range(len(NumSet)):
  NumSet[x] = int(NumSet[x])

print(NumSet)

Out = 0

def Check(Num):
  Num = str(Num)
  for x in range(len(Num)):
    x = Num[x]
    x = int(x)
    if x not in NumSet:
      return(False)
  return(True)

for a in NumSet:
  for b in NumSet:
    for c in NumSet:
      for d in NumSet:
        for e in NumSet:
          X = str((100*a + 10*b + c) * e)
          Y = str((100*a + 10*b + c) * d)
          Z = str(int(X) + 10 * int(Y))
          if len(X) == 3 and len(Y) == 3 and len(Z) == 4 and Check(X) and Check(Y) and Check(Z):
            Out += 1
Out = str(Out) + "\n"
#################################################################################################

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/crypt1/crypt1.out", "x")
else:
  File = open(r"crypt1.out", "x")
File.write(Out)
File.close()