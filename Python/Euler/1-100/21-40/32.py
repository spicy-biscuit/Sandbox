"""
32: Pandigital Products
"""

def Permutations(N):
    if N == 1:
        return(["1"])
    if N == 2:
        return(["21", "12"])
    ThisList = Permutations(N - 1)
    Out = []
    Add = str(N)
    for x in ThisList:
        for Index in range(N):
            String = x[:Index] + Add + x[Index:]
            Out.append(String)
        Out.append(x + Add)
    return(Out)

List = Permutations(9)

Set = set([])
for Item in List:
    # print(Item)
    for Index in range(1, 9):
        for Index2 in range(Index + 1, 9):
            a = int(Item[:Index])
            b = int(Item[Index:Index2])
            c = int(Item[Index2:])
            if a * b == c:
                print(a, b, c)
                Set.add(c)

print(sum(Set))