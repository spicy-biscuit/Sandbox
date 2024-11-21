"""
60: Prime Pair Sets
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

def NextPrime(OldList, OldN):
    AllPrimes = OldList
    Current = OldN
    while True:
        Current += 1
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

def FindAllSets(Sampling, DesiredSize):
    if DesiredSize == 1:
        List = []
        for x in Sampling:
            List.append([x])
        return(List)
    
    OutList = []
    for Index in range(0, len(Sampling) - DesiredSize + 1):
        This = Sampling[Index]
        List = Sampling[Index + 1:]
        All = FindAllSets(List, DesiredSize - 1)
        for x in All:
            OutList.append([This] + x)
    return(OutList)

def IsValid(Set, Pairings):
    for a in Set:
        for b in Set:
            if a == b:
                continue
            if a not in Pairings[b]:
                return(False)
    return(True)

def Intersection(List1, List2):
    List2 = set(List2)
    Out = []
    for x in List1:
        if x in List2:
            Out.append(x)
    return(Out)


ValidPairings = {}

Primes = ListOfPrimes(2)
SetPrimes = set(Primes)
Max = 2

while True:
    Primes = NextPrime(Primes, Max)
    Max = Primes[-1]
    SetPrimes.add(Max)

    ValidPairings[Max] = []

    for x in Primes:
        a = int(str(x) + str(Max))
        b = int(str(Max) + str(x))
        if IsPrime(a) and IsPrime(b):
            ValidPairings[Max].append(x)
            ValidPairings[x].append(Max)
    
    print(Max)
    if Max < 100:
        continue

    BREAKOUT = False
    for a in ValidPairings[Max]:
        for b in Intersection(ValidPairings[a], ValidPairings[Max]):
            for c in Intersection(Intersection(ValidPairings[b], ValidPairings[a]), ValidPairings[Max]):
                for d in Intersection(Intersection(Intersection(ValidPairings[b], ValidPairings[a]), ValidPairings[Max]), ValidPairings[Max]):
                    if a == b or a == c or Max == a or b == c or b == Max or c == Max or a == d or b == d or c == d or Max == d:
                        continue
                    if IsValid([Max, a, b, c, d], ValidPairings):
                        print(a, b, c, d, Max)
                        print(sum([Max, a, b, c, d]))
                        BREAKOUT = True

    if BREAKOUT:
        break