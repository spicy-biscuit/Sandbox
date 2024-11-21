"""
1195C: Basketball Exercise
"""

N = int(input())

FirstRow = tuple(map(int, input().split()))
SecondRow = tuple(map(int, input().split()))

from functools import cache

@cache
def Max(Index, CurrentRow):
  if CurrentRow == -1:
    return(max(Max(Index, 0), Max(Index, 1)))
  if Index == N:
    return(0)
  if Index == N - 1:
    if CurrentRow == 0:
      return(FirstRow[Index])
    else:
      return(SecondRow[Index])

  if CurrentRow == 0:
    return(max(FirstRow[Index] + Max(Index + 1, 1), FirstRow[Index + 1] + Max(Index + 2, 1)))
  else:
    return(max(SecondRow[Index] + Max(Index + 1, 0), SecondRow[Index + 1] + Max(Index + 2, 0)))

print(Max(0, -1))