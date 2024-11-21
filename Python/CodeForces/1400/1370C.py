"""
1370C: Number Game
"""

import math

def IsPowerOfTwo(Number):
  if Number == 1:
    return(True)
  if Number % 2 == 1:
    return(False)
  return(IsPowerOfTwo(int(Number / 2)))

def IsPrime(Number):
  if Number < 3:
    return(False)
  for x in range(2, math.ceil(math.sqrt(Number) + 3)):
    if x >= Number:
      break
    if Number % x == 0:
      return(False)
  return(True)

def Wins(Number):
  if Number == 1:
    print("FastestFinger")
    return(0)
  if Number == 2:
    print("Ashishgup")
    return(0)
    
  if Number % 2 == 1:
    print("Ashishgup")
    return(0)

  # if IsPowerOfTwo(Number):
  #   print("FastestFinger")
  #   return(0)

  if IsPrime(int(Number / 2)) and Number >= 6:
    print("FastestFinger")
    return(0)

  if IsPowerOfTwo(Number):
    print("FastestFinger")
    return(0)

  print("Ashishgup")

T = int(input())

for x in range(T):
  N = int(input())
  Wins(N)

"""
ACCEPTED!
>help
  >theory
"""