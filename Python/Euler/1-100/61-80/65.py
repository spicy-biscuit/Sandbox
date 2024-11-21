"""
65: Convergents of e
"""

def SumOfDigits(N):
    Out = 0
    N = str(N)
    for x in range(len(N)):
        Out += int(N[x])
    return(Out)

def GetValueE(N):
    if N == 1:
        return(2)
    if N % 3 == 0:
        N = N // 3
        return(2 * N)
    return(1)

# for x in range(1,10):
#     print(GetValueE(x))

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
  # if N in List:
  #   List.remove(N)
  
  return(List)

def intersection(lst1, lst2):
    lst3 = []
    for x in lst1:
       if x in lst2:
          lst3.append(x)
          lst2.remove(x)
    return(lst3)

def Reduce(Numerator, Denominator):
    Intersection = intersection(Divisors(Numerator), Divisors(Denominator))
    for x in Intersection:
        Numerator //= x
        Denominator //= x
    return([Numerator, Denominator])

def AddFractions(Num1, Den1, Num2, Den2):
   Num1 = Num1 * Den2 + Num2 * Den1
   Den1 = Den1 * Den2
#    Out = Reduce(Num1, Den2)
   Out = [Num1, Den2]
   return(Out)

Fraction = [1, 1]

def calculateE(N):
    N += 1
    List = [GetValueE(x) for x in reversed(range(1, N))]
    Fraction = [1, List[0]]
    List = List[1:]
    for x in List:
        print(Fraction)
        Fraction = AddFractions(x, 1, Fraction[0], Fraction[1])
        Fraction = [Fraction[1], Fraction[0]]
    # Fraction = AddFractions(1, 1, Fraction[0], Fraction[1])

    Fraction = [Fraction[1], Fraction[0]]
    return(Fraction)

print(SumOfDigits(calculateE(100)[0]))

