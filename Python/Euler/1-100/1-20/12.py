"""
12: Highly Divisible Triangular Number
"""

import math

def Divisors(N):
  List = []
  for x in range(1, math.ceil(math.sqrt(N)) + 5):
    if x * x == N:
      List.append(x)
      break
    if x * x > N:
      break
    if N % x == 0:
      List.append(x)
      List.append(int(N / x))

  List = list(set(List))
  List.sort()

  # List.remove(N)
  
  return(List)

N = 0
Triangle = 0
while True:
  N += 1
  Triangle += N
  d = len(Divisors(Triangle))
  if d >= 500:
    print(Triangle, d)
    break