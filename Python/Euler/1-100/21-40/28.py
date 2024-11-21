"""
28: Number Spiral Diagonals
"""

Size = 1001
# Size = 5

Real = Size // 2 + 1

Out = 0
for x in range(Real):
    y = 2 * x + 1
    # print(y ** 2)
    if y == 1:
        Out += 1
        continue
    Out += y ** 2
    Out += y ** 2 - y + 1
    Out += y ** 2 - 2 * y + 2
    Out += y ** 2 - 3 * y + 3

print()
print(Out)