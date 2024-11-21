"""
61: Cyclical Figurate Numbers
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

Triangles = []
Squares = []
Pentagons = []
Hexagons = []
Heptagons = []
Octagons = []

for x in range(1000, 10000):
    if TriangleCheck(x):
        Triangles.append(x)
    if SquareCheck(x):
        Squares.append(x)
    if PentagonCheck(x):
        Pentagons.append(x)
    if HexagonCheck(x):
        Hexagons.append(x)
    if HeptagonCheck(x):
        Heptagons.append(x)
    if OctagonCheck(x):
        Octagons.append(x)


All = Triangles + Squares + Pentagons + Hexagons + Heptagons + Octagons

P = [[] for x in range(9)]
P[0] = []
P[1] = []
P[2] = []
P[3] = Triangles
P[4] = Squares
P[5] = Pentagons
P[6] = Hexagons
P[7] = Heptagons
P[8] = Octagons

def Permutations(N):
    if N == 3:
        return(["3"])
    if N == 4:
        return(["43", "34"])
    ThisList = Permutations(N - 1)
    Out = []
    Add = str(N)
    for x in ThisList:
        for Index in range(N - 3):
            String = x[:Index] + Add + x[Index:]
            Out.append(String)
        Out.append(x + Add)
    return(Out)

AllPermutations = (Permutations(7))

def AllLists(Order, All, P):
    if len(Order) == 0:
        return(All)
    
    if Order[0] == 8:
        Out = All.copy()
        for x in P[8]:
            Out.append([x])
        return(AllLists(Order[1:], Out, P))
    
    Out = []
    for Sequence in All:
        LastNumber = Sequence[-1]
        Connecting = LastNumber % 100
        if Connecting < 10:
            continue
        for Next in P[Order[0]]:
            if Connecting == Next // 100:
                Out.append(Sequence + [Next])
    return(AllLists(Order[1:], Out, P))




for ORDER in AllPermutations:
    ORDER = list(ORDER)
    ORDER = list(map(int, ORDER))
    ORDER = [8] + ORDER
    This = (AllLists(ORDER, [], P))

    for x in This:
        if x[5] % 100 == x[0] // 100:
            print(sum(x))

    