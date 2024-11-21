"""
Daily Coding Problem: Problem #9 [Hard]

Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

from functools import cache

@cache
def Function(Tuple, Sum, Availible):
  if len(Tuple) == 0:
    return(Sum)
  if Availible:
    return(max(Function(Tuple[1:], Sum + Tuple[0], False), Function(Tuple[1:], Sum, True)))
  return(Function(Tuple[1:], Sum, True))

print(Function((5, 1, 1, 5), 0, True))