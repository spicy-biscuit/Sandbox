"""
23: Non-Abundant Sums
"""

import math
def IsAbundant(N):
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
  
  return(sum(List) > N)

Abundants = []

for x in range(10, 28123):
  if IsAbundant(x):
    Abundants.append(x)

print(Abundants)

Possible = [False for x in range(28150)]

for a in Abundants:
  for b in Abundants:
    if a + b < 28150:
      Possible[a + b] = True

Out = 0
for Index in range(1, 28150):
  if Possible[Index] == False:
    Out += Index

# print(Possible)
    
print(Out)