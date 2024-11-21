"""
2: Even Fibonacci Numbers
"""

a = 1
b = 1
Out = 0
while True:
  a, b = b, a + b
  if b > 4000000:
    break
  if b % 2 == 0:
    Out += b

print(Out)