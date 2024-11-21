"""
44: Pentagon Numbers
"""

import math

def Pentagon(N):
    return(int(N * (3 * N - 1) / 2))

def IsPentagonal(N):
    x = math.ceil(math.sqrt((2 / 3) * N))
    if abs(Pentagon(x) - N) <= 0.0005:
        return(True)
    return(False)

j = 1
Min = float('inf')
while True:
    j += 1
    if Pentagon(j) - Pentagon(j - 1) > Min + 100:
        break
    for i in range(1, j):
        Pj = Pentagon(j)
        Pi = Pentagon(i)
        if not (IsPentagonal(Pj + Pi) and IsPentagonal(Pj - Pi)):
            continue
        Difference = Pj - Pi
        if Difference < Min:
            print(j, i, Difference)
            Min = Difference
print(Min)
