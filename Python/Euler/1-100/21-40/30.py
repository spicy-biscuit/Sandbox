"""
30: Digit Fifth Powers
"""

def SumOfDigits(N):
  Out = 0
  N = str(N)
  for x in range(len(N)):
    Out += int(N[x]) ** 5
  return(Out)

Out = 0
for x in range(10, 1000000):
    if x == SumOfDigits(x):
       Out += x

print(Out)