Input = 29000000

import math

def Divisors(n):
  All = []
  for x in range(1, 51):
    if n % x == 0:
      All.append(int(n / x))
  All = list(set(All))
  # print(All)
  return(sum(All))

House = 100
while True:
  House += 1
  if House % 10000 == 0:
    print(House)
  if Divisors(House) * 11 >= Input:
    break

print(House)