"""
1285C: Fadi and LCM
"""

import math

X = int(input())

def Divisors(N):
  D = []
  for x in range(1, math.ceil(math.sqrt(N)) + 3):
    if x * x == N:
      D.append(x)
    if x > math.sqrt(N):
      continue
    elif N % x == 0:
      D.append(x)
  D = list(set(D))
  D.sort()
  return(D)

def Divisors1(N):
  D = []
  while True:
    if N == 1:
      break
    

def Multiply(List):
  Out = 1
  for x in List:
    Out *= x
  return(Out)

def LCM(a, b):
  A = Divisors1(a)
  B = Divisors1(b)
  print(A, B)
  Out = []
  for x in A:
    if x in B:
      B.remove(x)
    Out.append(x)

  for x in B:
    Out.append(x)

  return(Multiply(Out))

# D = Divisors(X)
# PRINT_SOMETHING = True
# for x in reversed(D):
#   a = x
#   b = int(X / a)
#   if LCM(a, b) == X:
#     print(a, b)
#     PRINT_SOMETHING = False
#     break

# if PRINT_SOMETHING:
#   print(1, X)

print(LCM(8, 3))