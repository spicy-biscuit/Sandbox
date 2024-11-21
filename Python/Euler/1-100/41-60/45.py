"""
45: Triangular, Pentagonal, and Hexagonal
"""

import math

def Triangle(N):
    return(int(N * (N + 1) / 2))

def Pentagon(N):
    return(int(N * (3 * N - 1) / 2))

def Hexagon(N):
    return(int(N * (2 * N - 1)))

def IsTriangular(N):
    x = math.floor(math.sqrt(2 * N))
    if Triangle(x) == N:
        return(True)
    return(False)

def IsPentagonal(N):
    x = math.ceil(math.sqrt((2 / 3) * N))
    if Pentagon(x) == N:
        return(True)
    return(False)

x = 1
while True:
    x += 1
    y = Hexagon(x)
    if IsTriangular(y) and IsPentagonal(y):
        print(y)
        if x != 143:
            break
