"""
Counting Fractions
"""

from functools import cache

def ListOfPrimes(N):
    AllPrimes = [2]
    for Current in range(3, N + 1):
        IsPrime = True
        for Prime in AllPrimes:
            if Prime * Prime > Current:
                break
            if Current % Prime == 0:
                IsPrime = False
                break
        if IsPrime:
            AllPrimes.append(Current)
    return(AllPrimes)

AllPrimes = ListOfPrimes(10**6+5)
SetAllPrimes = set(AllPrimes)

@cache
def IsPrime(N):
    if N in SetAllPrimes:
        return(True)
    return(False)

Dictionary = dict([])
DictionaryIndexes = set([])

# @cache
def PrimeFactors(N):
    Original = N
    # print(N)
    if N == 1:
        return(set([]))
    List = set([])
    X = -1
    while True:
        X += 1
        if N == 1:
            Dictionary[Original] = List
            DictionaryIndexes.add(Original)
            return(List)
        Y = AllPrimes[X]
        if N % Y == 0:
            List.add(Y)
            while True:
                N //= Y
                # print(N)
                if N % Y != 0:
                    if N in DictionaryIndexes:
                        for x in Dictionary[N]:
                            List.add(x)
                        return(List)
                    break

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

d = 10**6

#x - floor(x/n) is how many are NOT divisibly by n
#x is sample size
#n is the divisibility number

def Totient(N):
    if N % 2 == 0:
        X = Totient(int(N / 2))
        if N % 4 == 0:
            return(2 * X)
        return(X)

    Factors = PrimeFactors(N)
    
    Out = N

    for Factor in Factors:
        Out *= (Factor - 1)
        Out /= Factor

    # print(Out)

    return(round(Out))

Out = 0
for D in range(2, d + 1):
    if D % 1000 == 0:
        print(D)

    Out += Totient(D)
    # print(D, Totient(D))

print(Out)
