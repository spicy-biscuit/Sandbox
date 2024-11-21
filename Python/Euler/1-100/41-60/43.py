"""
43: Substring Divisibility
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

List = Permutations(9)
New = []
print("1")
for x in List:
    if x[0] != "0":
        New.append(x)
List.clear()
print("2")

Out = 0
for x in New:
    if int(x[1:4]) % 2 != 0:
        continue
    if int(x[2:5]) % 3 != 0:
        continue
    if int(x[3:6]) % 5 != 0:
        continue
    if int(x[4:7]) % 7 != 0:
        continue
    if int(x[5:8]) % 11 != 0:
        continue
    if int(x[6:9]) % 13 != 0:
        continue
    if int(x[7:10]) % 17 != 0:
        continue
    Out += int(x)

print(Out)