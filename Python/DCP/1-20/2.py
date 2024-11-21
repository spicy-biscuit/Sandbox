"""
Daily Coding Problem: Problem #2 [Hard]

Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def Function(List):
  Product = 1
  for x in List:
    Product *= x
  Output = []
  for x in List:
    Output.append(int(Product / x))
  return(Output)

def Function2(List):
  Output = []
  for x in range(len(List)):
    Append = 1
    for y in range(len(List)):
      if y == x:
        continue
      Append *= List[y]
    Output.append(Append)
  return(Output)

(Function2([x + 1 for x in range(1000)]))