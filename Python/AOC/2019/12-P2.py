Input = ["""<x=7, y=10, z=17>
<x=-2, y=7, z=0>
<x=12, y=5, z=12>
<x=5, y=-8, z=6>"""]

# Input = ["""<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>"""]

Input = Input[0].split("\n")

Moons = []

for x in Input:
  X = int(x[x.find("=") + 1:x.find(",")])
  x = x[x.find(" ") + 1:]
  Y = int(x[x.find("=") + 1:x.find(",")])
  x = x[x.find(" ") + 1:]
  Z = int(x[x.find("=") + 1:x.find(",")])
  Moons.append((X, Y, Z, 0, 0, 0))

def Energy(Moon):
  return((abs(Moon[0]) + abs(Moon[1]) + abs(Moon[2])) * (abs(Moon[3]) + abs(Moon[4]) + abs(Moon[5])))

from functools import cache

@cache
def Mini(FPos, FVel, SPos, SVel):
  if FPos > SPos:
    FVel -= 1
    SVel += 1
  if FPos < SPos:
    FVel += 1
    SVel -= 1
  return((FVel, SVel))

# @cache
def Gravity(FirstMoon, SecondMoon):
  FMX = FirstMoon[0]
  FMY = FirstMoon[1]
  FMZ = FirstMoon[2]
  SMX = SecondMoon[0]
  SMY = SecondMoon[1]
  SMZ = SecondMoon[2]
  FMXV = FirstMoon[3]
  FMYV = FirstMoon[4]
  FMZV = FirstMoon[5]
  SMXV = SecondMoon[3]
  SMYV = SecondMoon[4]
  SMZV = SecondMoon[5]
  
  Out = Mini(FMX, FMXV, SMX, SMXV)
  FMXV = Out[0]
  SMXV = Out[1]
  
  Out = Mini(FMY, FMYV, SMY, SMYV)
  FMYV = Out[0]
  SMYV = Out[1]
  
  Out = Mini(FMZ, FMZV, SMZ, SMZV)
  FMZV = Out[0]
  SMZV = Out[1]

  return([(FMX, FMY, FMZ, FMXV, FMYV, FMZV), (SMX, SMY, SMZ, SMXV, SMYV, SMZV)])

def Update(Moons):
  for First in range(4):
    for Second in range(First + 1, 4):

      Out = Gravity(Moons[First], Moons[Second])

      Moons[First] = Out[0]
      Moons[Second] = Out[1]

  for Moon in range(4):
    FirstMoon = Moons[Moon]
    FMX = FirstMoon[0]
    FMY = FirstMoon[1]
    FMZ = FirstMoon[2]
    FMXV = FirstMoon[3]
    FMYV = FirstMoon[4]
    FMZV = FirstMoon[5]
    FMX += FMXV
    FMY += FMYV
    FMZ += FMZV
    Moons[Moon] = (FMX, FMY, FMZ, FMXV, FMYV, FMZV)
    
  return(Moons)


XB = True
YB = True
ZB = True

XStart = (Moons[0][0], Moons[1][0], Moons[2][0], Moons[3][0], Moons[0][3], Moons[1][3], Moons[2][3], Moons[3][3])
YStart = (Moons[0][1], Moons[1][1], Moons[2][1], Moons[3][1], Moons[0][4], Moons[1][4], Moons[2][4], Moons[3][4])
ZStart = (Moons[0][2], Moons[1][2], Moons[2][2], Moons[3][2], Moons[0][5], Moons[1][5], Moons[2][5], Moons[3][5])
List = [0, 0, 0]
Counter = 0
while True:
  Counter += 1

  Update(Moons)

  if XB and (Moons[0][0], Moons[1][0], Moons[2][0], Moons[3][0], Moons[0][3], Moons[1][3], Moons[2][3], Moons[3][3]) == XStart:
    print(Counter)
    XB = False
    List[0] = Counter

  if YB and (Moons[0][1], Moons[1][1], Moons[2][1], Moons[3][1], Moons[0][4], Moons[1][4], Moons[2][4], Moons[3][4]) == YStart:
    print(Counter)
    YB = False
    List[1] = Counter

  if ZB and (Moons[0][2], Moons[1][2], Moons[2][2], Moons[3][2], Moons[0][5], Moons[1][5], Moons[2][5], Moons[3][5]) == ZStart:
    print(Counter)
    ZB = False
    List[2] = Counter

  if (not XB) and (not YB) and (not ZB):
    break

import math

print(math.lcm(List[0], List[1], List[2]))