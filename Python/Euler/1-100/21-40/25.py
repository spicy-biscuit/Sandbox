"""
25: 1000-Digit Fibonacci Number
"""

a = 1
b = 1
Index = 1
while True:
    a, b = b, a + b
    Index += 1
    if a >= 10 ** (1000 - 1):
        print(Index)
        break