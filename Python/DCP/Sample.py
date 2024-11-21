from functools import cache

@cache
def Staircase(N, X):
  if N == 0:
    return(1)
  Output = 0
  for x in X:
    if N >= x:
      Output += Staircase(N - x, X)
  return(Output)

print(Staircase(100, (1, 2)))
