"""
Requires: Math module
Time Complexity: O(log(N) * N)
Memory Complexity: ~O(logN)
Input Type: Integer

Returns a list of all primes equal to or less than N
Assumes N > 2

Second function updates a list of primes to expand the maximum.
OldList = UpdateListOfPrimes(OldList, OldMax, NewMax)

Third function adds one prime onto the end of the list.
OldList = NextPrime(OldList, OldList[-1])
^^ Assuming list is sorted (which is should be)
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