"""
57: Square Root Convergents
"""

def Iterate(List):
    a = List[0]
    b = List[1]
    return([a + 2 * b, a + b])

Current = [0, 0]
Out = 0
for x in range(1, 1001):
    if x == 1:
        Current = [3, 2]
    else:
        Current = Iterate(Current)
    a = Current[0]
    b = Current[1]
    a = str(a)
    b = str(b)
    if len(a) > len(b):
        Out += 1

print(Out)