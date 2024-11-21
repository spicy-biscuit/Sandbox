"""
3: Largest Prime Factor
"""

Number = 600851475143

i = 2
while True:
  if Number == 1:
    break
  if Number % i == 0:
    Number //= i
  else:
    i += 1

print(i)