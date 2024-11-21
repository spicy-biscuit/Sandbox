"""
58: Spiral Primes
"""

import math

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

def Diagonals(SideLength):
    if SideLength == 1:
        return([1])
    List = []
    for Change in range(0, 4):
        Change = Change * (SideLength - 1)
        List.append(SideLength ** 2 - Change)
    return(List)

SideLength = 1

All = 1
Primes = 0

while True:
    SideLength += 2
    All += 4
    This = Diagonals(SideLength)
    for x in This:
        if IsPrime(x):
            Primes += 1
    if Primes / All < 0.1:
        print(SideLength)
        break