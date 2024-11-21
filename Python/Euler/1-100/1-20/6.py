"""
6: Sum Square Difference
"""

a = 0
b = 0

for x in range(1, 101):
  a += x
  b += x ** 2

a = a ** 2

print(a - b)