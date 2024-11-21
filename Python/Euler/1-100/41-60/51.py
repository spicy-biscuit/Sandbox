"""
51: Prime Replacements
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

def STRING(List):
    Out = ""
    for x in List:
        Out = Out + x
    return((Out))

def Replace(String):
    Indexes = []
    for Index in range(len(String)):
        if String[Index] == "*":
            Indexes.append(Index)
    OutList = []
    if String[0] == "*":
        for x in range(1, 10):
            NewList = list(String)
            for y in Indexes:
                NewList[y] = str(x)
            OutList.append(STRING(NewList))
    else:
        for x in range(0, 10):
            NewList = list(String)
            for y in Indexes:
                NewList[y] = str(x)
            OutList.append(STRING(NewList))
    return(OutList)

def Function1(ReplaceThese):
    if len(ReplaceThese) == 0:
        return([])
    if len(ReplaceThese) == 1:
        return([ReplaceThese, []])
    List = Function1(ReplaceThese[1:])
    OutList = List.copy()
    for x in List:
        OutList.append([ReplaceThese[0]] + x)
    return(OutList)

def ReplaceWithAsterisk(Number, ReplaceWith):
    Number = list(str(Number))
    for x in ReplaceWith:
        Number[x] = "*"
    Number = STRING(Number)
    return(Number)

def CountPrimes(List, SetPrimes):
    # print(List)
    Out = 0
    for x in List:
        if int(x) in SetPrimes:
            Out += 1
    return(Out)


def FindFamilies(Number, SetPrimes):
    Ones = []
    Twos = []
    Zeroes = []
    String = str(Number)
    for x in range(len(String)):
        if String[x] == "0":
            Zeroes.append(x)
        if String[x] == "1":
            Ones.append(x)
        if String[x] == "2":
            Twos.append(x)

    Zeroes = Function1(Zeroes)
    Ones = Function1(Ones)
    Twos = Function1(Twos)
    for x in range(len(Zeroes)):
        Zeroes[x] = ReplaceWithAsterisk(Number, Zeroes[x])
        if Zeroes[x].find("*") == -1:
            Zeroes[x] = 0
            continue
        Zeroes[x] = Replace(Zeroes[x])
        Zeroes[x] = CountPrimes(Zeroes[x], SetPrimes)
    for x in range(len(Ones)):
        Ones[x] = ReplaceWithAsterisk(Number, Ones[x])
        if Ones[x].find("*") == -1:
            Ones[x] = 0
            continue
        Ones[x] = Replace(Ones[x])
        Ones[x] = CountPrimes(Ones[x], SetPrimes)
    for x in range(len(Twos)):
        Twos[x] = ReplaceWithAsterisk(Number, Twos[x])
        if Twos[x].find("*") == -1:
            Twos[x] = 0
            continue
        Twos[x] = Replace(Twos[x])
        Twos[x] = CountPrimes(Twos[x], SetPrimes)

    # print(Zeroes)
    # print(Ones)
    # print(Twos)
    Zeroes.append(0)
    return(max(Zeroes + Ones + Twos))


Primes = ListOfPrimes(100)
PrimeSet = set(Primes)
Max = 100

# print(FindFamilies("13", PrimeSet))

Current = 9
while True:
    Current += 1
    if Current > Max - 20:
        Primes = UpdateListOfPrimes(Primes, Max, Max * 10)
        PrimeSet = set(Primes)
        Max *= 10
        print("MAX:", Max)
    This = FindFamilies(str(Current), PrimeSet)
    if This >= 8:
        print(Current)
        break



