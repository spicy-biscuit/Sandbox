"""
55: Lychrel Numbers
"""

def IsPalindrome(N):
    N = str(N)
    if N == N[::-1]:
        return(True)
    return(False)

def Iterate(N):
    N1 = str(N)
    N1 = N1[::-1]
    N1 = int(N1)
    return(N + N1)

Out = 0
for x in range(1, 10000):

    Lychrel = True
    for ITERATION in range(60):
        x = Iterate(x)
        if IsPalindrome(x):
            Lychrel = False
    if Lychrel:
        Out += 1
    
print(Out)