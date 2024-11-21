"""
50: Consecutive Prime Sum
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

Primes = ListOfPrimes(1000000)
IsPrime = [False for x in range(1000000)]

for x in Primes:
    IsPrime[x] = True

a = 0
MaxLength = 0
for x in Primes:
    a += x
    MaxLength += 1
    if a > 1000000:
        print(MaxLength)
        break

NumPrimes = len(Primes)

Out = 0
for Length in range(4, MaxLength + 1):
    Index = -1
    Sum = sum(Primes[:Length])
    Valid = False
    while True:
        Index += 1
        if Index + Length >= NumPrimes - 1:
            break
        if Sum > 1000000 - 1:
            continue
        if IsPrime[Sum]:
            Valid = True
            This = Sum
            break
        Sum -= Primes[Index]
        Sum += Primes[Index + Length]
    if Valid:
        Out = This
        print(Out)

