"""
69: Totient Maximum
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

AllPrimes = ListOfPrimes(1000000+10000)
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

    return(Out)


Max = 0
Out = 0
for x in range(2, 1000000 + 1):
# for x in range(2, 10 + 1):
    if x % 1000 == 0:
        print(x)
    y = x / Totient(x)
    # print(x, y)
    # print(x, PrimeFactors(x))
    if y > Max:
        Max = y
        Out = x
        print("-------------------")
        print(Out, Max)
        print("-------------------")

print(Out)