import math

def SumFunction(n):
  Sum = 0
  for x in range(n):
    Sum += 1/(2 * math.floor(math.sqrt(n+1))+1)
  return(Sum)

Counter = 0
for x in range(1000000):
  x+=1
  y = SumFunction(x)
  if abs(y - math.floor(y)) < 0.0000001:
    print(y)
    Counter += 1

print(Counter)