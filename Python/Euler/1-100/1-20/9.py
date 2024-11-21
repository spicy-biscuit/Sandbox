"""
9: Special Pythagorean Triplet
"""

Break = False
for a in range(1, 1001):
  for b in range(a, 1001):
    c = 1000 - b - a
    if a ** 2 + b ** 2 == c ** 2:
      print(a * b * c)
      Break = True
      break
  if Break:
    break