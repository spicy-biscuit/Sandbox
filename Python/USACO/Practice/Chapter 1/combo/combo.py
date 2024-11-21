'''
ID: ethanfung8
LANG: PYTHON3
PROG: combo
'''

HOME_FILES = False
OUTPUT_TO_FILES = True

if HOME_FILES:
  File = open(r"USACO/Practice/Chapter 1/combo/combo.in", "r")
else:
  File = open(r"combo.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

if Input[-1].isspace():
  Input = Input[:-1]
  
#################################################################################################

N = int(Input[0])
JohnCombo = Input[1].split()
MasterCombo = Input[2].split()

for x in range(3):
  JohnCombo[x] = int(JohnCombo[x])
  MasterCombo[x] = int(MasterCombo[x])

AllCombos = set([])

def Change(Tuple):
  Tuple = list(Tuple)
  for x in range(3):
    This = Tuple[x]
    for y in range(2):
      if This < 1:
        This += N
      if This > N:
        This -= N
    Tuple[x] = This
  return(tuple(Tuple))

for FirstChange in range(-2, 3):
  for SecondChange in range(-2, 3):
    for ThirdChange in range(-2, 3):
      NewJohn = (JohnCombo[0] + FirstChange, JohnCombo[1] + SecondChange, JohnCombo[2] + ThirdChange)
      NewMaster = (MasterCombo[0] + FirstChange, MasterCombo[1] + SecondChange, MasterCombo[2] + ThirdChange)
      AllCombos.add(Change(NewJohn))
      AllCombos.add(Change(NewMaster))

Out = str(len(AllCombos)) + "\n"

#################################################################################################

if OUTPUT_TO_FILES:
  if HOME_FILES:
    File = open(r"USACO/Practice/Chapter 1/combo/combo.out", "x")
  else:
    File = open(r"combo.out", "x")
  File.write(Out)
  File.close()