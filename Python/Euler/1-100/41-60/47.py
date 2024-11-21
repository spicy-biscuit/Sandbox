"""
47: Distinct Prime Factors
"""

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

def PrimeFactors(N, Primes):
    Count = 0
    for x in Primes:
        if N == 1:
            break
        if N % x == 0:
            Count += 1
            while True:
                N //= x
                if N % x != 0:
                    break
    return(Count)

Primes = ListOfPrimes(100)
Max = 100

Required = 4
Count = 0
Current = 5
while True:
    Current += 1

    if Current + Required + 20 > Max:
        Primes = UpdateListOfPrimes(Primes, Max, Max * 10)
        Max *= 10

    IsOut = True
    if PrimeFactors(Current, Primes) >= Required:
        Count += 1
    else:
        Count = 0
    if Count == 3:
        print(Current)
    if Count == Required:
        print()
        print(Current - Required + 1)
        break
