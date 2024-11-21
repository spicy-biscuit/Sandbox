Input = 7347
# Input = 42 #21,61
# Input = 18 #33,45

SerialID = Input

from functools import cache

@cache
def FindPowerLevel(X, Y, Serial):
  RackID = X + 10
  Out = RackID * Y
  Out += Serial
  Out *= RackID
  if Out < 100:
    Out = 0
  else:
    # print(Out, int(str(Out)[-3]))
    Out = int(str(Out)[-3])
  Out -= 5
  return(Out)

# print(FindPowerLevel(122, 79, 57))
# print(FindPowerLevel(217, 196, 39))
# print(FindPowerLevel(101, 153, 71))

def FindTotal(X, Y, Serial):
  Out = 0
  for x in range(3):
    for y in range(3):
      Out += FindPowerLevel(X + x, Y + y, Serial)
  return(Out)

Max = 0
Out = (0, 0)
for X in range(1, 299):
  for Y in range(1, 299):
    Val = FindTotal(X, Y, SerialID)
    if Val > Max:
      Max = Val
      Out = (X, Y)
      print(Out, Max)

print(str(Out[0]) + "," + str(Out[1]), Max)