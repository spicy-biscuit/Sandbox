"""
20: Factorial Digit Sum
"""

def Factorial(N):
  Out = 1
  for x in range(2, N):
    Out *= x
  return(Out)

def SumOfDigits(N):
  Out = 0
  N = str(N)
  for x in range(len(N)):
    Out += int(N[x])
  return(Out)

X = Factorial(100)
print(SumOfDigits(X))