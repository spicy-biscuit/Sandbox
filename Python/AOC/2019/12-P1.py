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

def Update(Moons):
  for First in range(4):
    for Second in range(First + 1, 4):
      # print(First, Second)
      FirstMoon = Moons[First]
      SecondMoon = Moons[Second]
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

      if FMX > SMX:
        FMXV -= 1
        SMXV += 1
      if FMX < SMX:
        FMXV += 1
        SMXV -= 1

      if FMY > SMY:
        FMYV -= 1
        SMYV += 1
      if FMY < SMY:
        FMYV += 1
        SMYV -= 1

      if FMZ > SMZ:
        FMZV -= 1
        SMZV += 1
      if FMZ < SMZ:
        FMZV += 1
        SMZV -= 1

      Moons[First] = (FMX, FMY, FMZ, FMXV, FMYV, FMZV)
      Moons[Second] = (SMX, SMY, SMZ, SMXV, SMYV, SMZV)

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

for x in range(1000):
  Update(Moons)

Total = 0
for x in Moons:
  Total += Energy(x)
print(Total)