"""
7:
"""

Primes = [2]
Count = 1

Current = 2
while True:
  if Count == 10001:
    break
  Current += 1
  IsPrime = True
  for x in Primes:
    if Current % x == 0:
      IsPrime = False
      break
  if IsPrime:
    Count += 1
    Primes.append(Current)

print(Primes[-1])