"""
49: Prime Permutations
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

Primes = ListOfPrimes(10 ** 4)
for x in ListOfPrimes(10 ** 3):
    Primes.remove(x)

SetPrimes = set(Primes)

def IsPermutations(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    a = list(a)
    b = list(b)
    c = list(c)
    a.sort()
    b.sort()
    c.sort()
    if a == b and b == c:
        return(True)

for a in Primes:
    for b in Primes:
        if b <= a:
            continue
        c = b + b - a
        if b + b - a in SetPrimes and IsPermutations(a, b, c):
            print(str(a) + str(b) + str(c))
