"""
10: Summation of Primes
"""

Primes = [2]

for x in range (3, 2000000):
  # if x % 10000 == 0:
  #   print(x)
  IsPrime = True
  for y in Primes:
    if y * y > x:
      break
    if x % y == 0:
      IsPrime = False
      break
  if IsPrime:
    Primes.append(x)

print(sum(Primes))