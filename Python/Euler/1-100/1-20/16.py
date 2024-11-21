"""
16: Power Digit Sum
"""

x = str(2 ** 1000)
Out = 0
for y in list(x):
  Out += int(y)
print(Out)