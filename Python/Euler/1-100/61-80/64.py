"""
64: Odd Period Square Roots
"""

import math

def PeriodLength(N):

    if round(math.sqrt(N)) ** 2 == N:
        return(0)

    Set = []

    Current = (math.floor(math.sqrt(N)), 1, N, math.floor(math.sqrt(N)))
    #(a, b, c, d) means:
    # a, b/(sqrt(c) - d)
    while True:
        # print(Current)
        if Current in Set:
            return(len(Set) - Set.index(Current))
        Set.append(Current)

        a = Current[0]
        b = Current[1]
        c = Current[2]
        d = Current[3]

        e = math.sqrt(c) + d
        f = (c-d**2)//b

        g = e/f

        Adder = 0
        while True:
            if g > 1:
                g -= 1
                Adder += 1
                continue
            break

        Current = (Adder, f, c, Adder * f - d)

Out = 0
for x in range(2, 10000 + 1):
    if PeriodLength(x) % 2 == 1:
        Out += 1
print(Out)