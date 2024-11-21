"""
37: Truncatable Primes
"""

import math

def TruncateLeft(N):
    N = str(N)
    Out = []
    for x in range(len(N)):
        Out.append(int(N[x:]))
        # if x != 0:
        #     Out.append(int(N[:x]))
    return(Out)

def TruncateRight(N):
    N = str(N)
    Out = [int(N)]
    for x in range(len(N)):
        # Out.append(int(N[x:]))
        if x != 0:
            Out.append(int(N[:x]))
    return(Out)

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

def IsPrime(N):
    if N < 2:
        return(False)
    for x in range(2, N):
        if x * x > N:
            break
        if x >= N:
            break
        if N % x == 0:
            return(False)
    return(True)

Primes = ListOfPrimes(100)
GlobalMax = [100]

def IsTruncatableLeft(N, InPrimes):
    # if N > GlobalMax[0]:
    #     InPrimes = UpdateListOfPrimes(InPrimes, GlobalMax[0], GlobalMax[0] * 10)
    #     GlobalMax[0] *= 10
    List = TruncateLeft(N)
    for x in List:
        if not IsPrime(x):
            return(False)
    return(True)

def IsTruncatableRight(N, InPrimes):
    # if N > GlobalMax[0]:
    #     InPrimes = UpdateListOfPrimes(InPrimes, GlobalMax[0], GlobalMax[0] * 10)
    #     GlobalMax[0] *= 10
    List = TruncateRight(N)
    for x in List:
        if not IsPrime(x):
            return(False)
    return(True)

# print(IsTruncatableLeft(79, Primes))
# print(IsTruncatableRight(79, Primes))

TwoDigits = []
OutList = []

for x in range(10, 100):
    if IsTruncatableLeft(x, Primes) or IsTruncatableRight(x, Primes):
        TwoDigits.append(x)
    if IsTruncatableLeft(x, Primes) and IsTruncatableRight(x, Primes):
        OutList.append(x)

New = TwoDigits

Counter = 0
while True:
    Old = New
    New = []
    # print(Old)
    for x in Old:
        for y in [x for x in range(1, 10)]:
            z = int(str(x) + str(y))
            if IsTruncatableLeft(z, Primes) or IsTruncatableRight(z, Primes):
                New.append(z)
            if IsTruncatableLeft(z, Primes) and IsTruncatableRight(z, Primes) and z not in OutList:
                OutList.append(z)
            z = int(str(y) + str(x))
            if IsTruncatableLeft(z, Primes) or IsTruncatableRight(z, Primes):
                New.append(z)
            if IsTruncatableLeft(z, Primes) and IsTruncatableRight(z, Primes) and z not in OutList:
                OutList.append(z)
    # print(OutList)
    # print()
    if len(OutList) >= 11:
        break

print(sum(OutList))