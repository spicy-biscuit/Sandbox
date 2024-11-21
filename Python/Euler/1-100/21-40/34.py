"""
34: Digit Factorials
"""

from functools import cache

@cache
def Factorial(N):
    if N == 0:
        return(1)
    return(N * Factorial(N - 1))

def SumOfDigits(N):
    Out = 0
    N = str(N)
    for x in range(len(N)):
        Out += Factorial(int(N[x]))
    return(Out)

# Real = 0
def Function(List, Index):
    if Index == 10:
        # print(List, sum(List))
        #Something idk
        Sum = 0
        for Index in range(10):
            Sum += List[Index] * Factorial(Index)
        OldSum = Sum
        Sum = list(str(Sum))
        Sum = list(map(int, Sum))
        Sum.sort()
        New = []
        for Index in range(10):
            This = List[Index]
            for x in range(This):
                New.append(Index)
        New.sort()
        if Sum == New:
            if OldSum != 1 and OldSum != 2:
                return(OldSum)
        return(0)
            
    Sum = sum(List)
    Out = 0
    for x in range(8 - Sum + 1):
        New = List.copy()
        New[Index] = x
        Out += Function(New, Index + 1)
    return(Out)

print(Function([0 for x in range(10)], 0))
# print(Real)