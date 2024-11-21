"""
Creation Functions:

Requires: None
Time Complexity: O(1)
Memory Complexity: O(1)
Input Type: Integer
Output Type: Integer


Check Functions:

Requires: Math, Creation functions
Time Complexity: O(1)
Memory Complexity: O(1)
Input Type: Integer
Output Type: Boolean
"""

def Triangle(N):
    return((N * (N + 1)) // 2)

def Square(N):
    return(N * N)

def Pentagon(N):
    return((N * (3 * N - 1)) // 2)

def Hexagon(N):
    return(N * (2 * N - 1))

def Heptagon(N):
    return((N * (5 * N - 3)) // 2)

def Octagon(N):
    return(N * (3 * N - 2))


import math

def TriangleCheck(N):
    x = math.floor(math.sqrt(2 * N))
    if Triangle(x) == N:
        return(True)
    return(False)

def SquareCheck(N):
    x = round(math.sqrt(N))
    if Square(x) == N:
        return(True)
    return(False)

def PentagonCheck(N):
    x = math.ceil(math.sqrt(2 * N / 3))
    if Pentagon(x) == N:
        return(True)
    return(False)

def HexagonCheck(N):
    x = math.ceil(math.sqrt(2 * N / 4))
    if Hexagon(x) == N:
        return(True)
    return(False)

def HeptagonCheck(N):
    x = math.ceil(math.sqrt(2 * N / 5))
    if Heptagon(x) == N:
        return(True)
    return(False)

def OctagonCheck(N):
    x = math.ceil(math.sqrt(2 * N / 6))
    if Octagon(x) == N:
        return(True)
    return(False)