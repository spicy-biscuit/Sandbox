"""
Daily Coding Problem: Problem #1 [Easy]

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def Function(List, k):
  for x in range(len(List) - 1):
    for y in range(x + 1, len(List)):
      if List[x] + List[y] == k:
        return(True)
  return(False)

print(Function([10, 15, 3, 7], 17))