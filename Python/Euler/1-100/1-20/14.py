"""
14: Longest Collatz Sequence
"""

from functools import cache

@cache
def Collatz(N):
  if N == 1:
    return(1)
  if N % 2 == 0:
    return(1 + Collatz(int(N / 2)))
  return(1 + Collatz(3 * N + 1))

Max = 0
Out = 0
for x in range(1, 1000000):
  This = Collatz(x)
  if This > Max:
    Max = This
    Out = x

print(Out)