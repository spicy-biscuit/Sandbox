"""
70: Totient Permutation
"""
import math
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

AllPrimes = ListOfPrimes(10000+5)
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

    return(round(Out))

def IsPermutation(x, y):
    x = list(str(x))
    y = list(str(y))
    x.sort()
    y.sort()
    if x == y:
        return(True)
    return(False)

AllPrimes.reverse()
# print((AllPrimes))

NewAllPrimes = AllPrimes[:10000]

List = []
for x in NewAllPrimes:
    print(x)
    for y in NewAllPrimes:
        if x < 1000 or y < 1000:
            break
        # print(y)
        z = x * y
        if z > 10000000:
            continue
        List.append([z/Totient(z), z, x, y])
        # break

def SortFunc(List):
    return(List[0])

List.sort(key=SortFunc)
# List.reverse()
# print(List)
for x in List:
    n = x[1]
    Tn = Totient(n)
    if IsPermutation(Tn, n):
        print("ANSWER:", n)
        break

print(Totient(n))
print(n/Totient(n))