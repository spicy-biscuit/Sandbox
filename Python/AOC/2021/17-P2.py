Input = [153, 199, -114, -75]
# Input = [20, 30, -10, -5]

X1 = Input[0]
X2 = Input[1]
Y1 = min(Input[2], Input[3])
Y2 = max(Input[2], Input[3])

TargetTiles = []
for x in range(X1, X2 + 1):
  for y in range(Y1, Y2 + 1):
    TargetTiles.append((x, y))
TargetTiles = set(TargetTiles)

# print(TargetTiles)

def Simulate(XVelocity, YVelocity):
  XPos = 0
  YPos = 0
  while True:
    XPos += XVelocity
    YPos += YVelocity
    if XVelocity > 0:
      XVelocity -= 1
    elif XVelocity < 0:
      XVelocity += 1
    YVelocity -= 1
    if (XPos, YPos) in TargetTiles:
      return(True)
    if XPos > X2 + 100 or YPos < Y2 - 100:
      return(False)

Count = 0
for YVelocity in range(Y1 - 100, -1 * Y1 + 10):
  for XVelocity in range(X2 + 100):
    # print(XVelocity, YVelocity, Simulate(XVelocity, YVelocity))
    if Simulate(XVelocity, YVelocity):
      Count += 1
print(Count)