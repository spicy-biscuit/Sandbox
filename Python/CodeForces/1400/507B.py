"""
507B: Amr and Pins
"""

import math

Input = list(map(int, input().split()))

R = Input[0]

X = Input[1]
Y = Input[2]

XT = Input[3]
YT = Input[4]

Distance = math.sqrt(abs(XT - X) ** 2 + abs(YT - Y) ** 2)

# print(Distance)

Steps = 0
while True:
  if abs(Distance - 0) <= 0.0000005:
    break
    
  # if abs(Distance - 2 * R) <= 0.005:
  #   Steps += 1
  #   break

  if Distance > 0 and Distance < 2 * R + 0.0000005:
    Steps += 1
    break

  # if Distance > 2 * R and Distance < 4 * R:
  #   Steps += 2
  #   break

  Steps += 1
  Distance -= 2 * R

print(Steps)

"""
ACCEPTED!
"""