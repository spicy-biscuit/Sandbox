"""
24: Lexicographic Permutations
"""

def Permutations(N):
    if N == 0:
        return(["0"])
    if N == 1:
        return(["01", "10"])
    ThisList = Permutations(N - 1)
    Out = []
    Add = str(N)
    for x in ThisList:
        for Index in range(N):
            String = x[:Index] + Add + x[Index:]
            Out.append(String)
        Out.append(x + Add)
    return(Out)

x = (Permutations(9))
x.sort()
print(x[1000000-1])