"""
35: Circular Primes
"""

import math

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
    return(set(AllPrimes))

def Rotate(N):
    N = str(N)
    Out = []
    for x in range(len(N)):
        Out.append(int(N[x:] + N[:x]))
    return(Out)

Primes = ListOfPrimes(1000000)

IsPrime = [False for x in range(1000000)]

for x in Primes:
    IsPrime[x] = True

Count = 0
for x in range(1, 1000000):
    List = Rotate(x)
    IsCircular = True
    for x in List:
        if not IsPrime[x]:
            IsCircular = False
    if IsCircular:
        Count += 1
print(Count)
