"""
Daily Coding Problem: Problem #14 [Medium]

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random

InCircle = 0
OutCircle = 0
Equal = 0
LastValue = 0
ThisValue = 0
Counter = 0
while True:
  Counter += 1
  x = random.random()
  y = random.random()
  x = 2 * x - 1
  y = 2 * y - 1
  if x**2 + y**2 < 1:
    InCircle += 1
  else:
    OutCircle += 1
  LastValue = ThisValue
  ThisValue = 4 * (InCircle/(InCircle + OutCircle))
  if str(LastValue)[:5] == str(ThisValue)[:5]:
    Equal += 1
  else:
    Equal = 0
  if Equal == 100000:
    break
  if Counter % 10000 == 0:
    print(Equal, ThisValue)
print(ThisValue)