"""
41: Pandigital Prime
"""

def IsPandigital(N):
    N = str(N)
    N = list(N)
    N.sort()
    return(N == [x for x in range(1, len(N) + 1)])

def IsPrime(N):
    if N < 2:
        return(False)
    for x in range(2, N):
        if x * x > N:
            break
        if x >= N:
            break
        if N % x == 0:
            return(False)
    return(True)

def Permutations(N):
    if N == 1:
        return(["1"])
    if N == 2:
        return(["12", "21"])
    ThisList = Permutations(N - 1)
    Out = []
    Add = str(N)
    for x in ThisList:
        for Index in range(N):
            String = x[:Index] + Add + x[Index:]
            Out.append(String)
        Out.append(x + Add)
    return(Out)


for Length in reversed(range(1, 10)):
    List = Permutations(Length)
    List.sort(reverse=True)
    BREAKOUT = False
    for x in List:
        x = int(x)
        if IsPrime(x):
            print(x)
            BREAKOUT = True
            break
    if BREAKOUT:
        break
