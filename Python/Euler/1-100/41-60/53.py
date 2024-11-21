"""
53: Combinatoric Selections
"""

from functools import cache

@cache
def Factorial(N):
    Out = 1
    for x in range(1, N + 1):
        Out *= x
    return(Out)

def Choose(N, R):
    Out = Factorial(N)
    Out //= Factorial(R)
    Out //= Factorial(N - R)
    return(Out)

Out = 0
for N in range(1, 101):
    for R in range(1, N + 1):
        if Choose(N, R) > 10 ** 6:
            Out += 1

print(Out)