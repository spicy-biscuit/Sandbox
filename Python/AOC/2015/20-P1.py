Input = 29000000

import math

def Divisors(n):
  All = []
  for x in range(1, math.ceil(math.sqrt(n)) + 1):
    if n % x == 0:
      All.append(x)
      All.append(int(n / x))
  All = list(set(All))
  # print(All)
  return(sum(All))

House = 0
while True:
  House += 1
  if House % 10000 == 0:
    print(House)
  if Divisors(House) * 10 >= Input:
    break

print(House)