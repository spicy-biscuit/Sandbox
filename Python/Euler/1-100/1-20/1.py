"""
1: Multiples of 3 or 5
"""

Out = 0

for x in range(1000):
  if x % 3 == 0 or x % 5 == 0:
    Out += x

print(Out)