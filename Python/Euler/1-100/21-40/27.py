"""
27: Quadratic Primes
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

All = ListOfPrimes(2011000) #10k for extra space :P
All = set(All)
IsPrime = [False for x in range(2011000)]
for x in All:
    IsPrime[x] = True

Max = 0
Out = 0
for a in range(-1000 + 1, 1000):
    if a % 100 == 0:
        print(a)
    for b in range(-1000 + 1, 1000):
        n = -1
        Count = 0
        while True:
            n += 1
            This = n * n + a * n + b
            if IsPrime[This]:
                Count += 1
            else:
                break
        if Count > Max:
            Max = Count
            Out = a * b

print(Out)