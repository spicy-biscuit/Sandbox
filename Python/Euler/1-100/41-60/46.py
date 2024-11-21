"""
46: Goldbach's Other Conjecture
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
    return(AllPrimes)

def UpdateListOfPrimes(OldList, OldN, N):
    AllPrimes = OldList
    for Current in range(OldN + 1, N + 1):
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

def isSquare(N):
    Root = math.floor(math.sqrt(N))
    for x in range(Root - 1, Root + 1):
        if x ** 2 == N:
            return(True)
    return(False)

Primes = ListOfPrimes(100)
SetPrimes = set(Primes)
Max = 100

Current = 7

while True:
    Current += 2
    if Current > Max - 20:
        Primes = UpdateListOfPrimes(Primes, Max, Max * 2)
        SetPrimes = set(Primes)
        Max *= 2
    
    if Current in SetPrimes:
        continue
    
    IsCounterExample = True
    for x in Primes[1:]:
        if x > Current:
            break
        New = Current - x
        New = int(New / 2)
        if isSquare(New):
            IsCounterExample = False
            print(Current, x, math.sqrt(New))
            break
    if IsCounterExample:
        print(Current)
        break