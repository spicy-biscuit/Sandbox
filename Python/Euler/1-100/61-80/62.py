"""
62: Cubic Permutations
"""

CurrentLength = 1
Current = 0

while True:
    CurrentLength += 1
    List = []
    OldCurrent = Current

    while True:
        Current += 1
        Cubed = Current ** 3
        if len(str(Cubed)) > CurrentLength:
            break

        if len(str(Cubed)) == CurrentLength:
            This = list(str(Cubed))
            This.sort()
            This = tuple(This)
            List.append(This)

    BREAKOUT = False
    New = []
    for x in List:
        if List.count(x) == 5:
            BREAKOUT = True
            New.append(x)
    Current -= 10
    if Current < 2:
        Current = 1

    if BREAKOUT:
        break

# print(New)

# OldCurrent = 0
while True:
    OldCurrent += 1
    Cubed = OldCurrent ** 3
    if len(str(Cubed)) > CurrentLength:
        break

    This = list(str(Cubed))
    This.sort()
    This = tuple(This)
    if This in New:
        print(OldCurrent ** 3)
        break