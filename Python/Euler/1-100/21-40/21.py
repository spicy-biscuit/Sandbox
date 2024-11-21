"""
21: Amicable Numbers
"""

import math
def Divisors(N):
  List = []
  #iterate through everying up to the sqrt of N
  for x in range(1, math.ceil(math.sqrt(N)) + 5):
    #if x is sqrt(N) then add x, then break out
    if x * x == N:
      List.append(x)
      break
    #if x > sqrt(N), get out
    if x * x > N:
      break
    #if N divisible by x, add x and N/x
    if N % x == 0:
      List.append(x)
      List.append(int(N / x))

  #Remove all duplicates
  List = list(set(List))
  #OPTIONAL, RECOMMENDED: sort list
  List.sort()

  #OPTIONAL: remove N from divisors
  if N in List:
    List.remove(N)
  
  return(sum(List))

Out = 0
for a in range(1, 10000):
  b = Divisors(a)
  if a == b:
    continue
  if Divisors(b) == a:
    Out += a
    # print(a, b)

print(Out)