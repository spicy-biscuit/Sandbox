"""
Requires: None
Time Complexity: O(n!)
Memory Complexity: O(n!)
Input Type: Integer
Output Type: List

Returns a list of all permutations of 0-N. Includes N and 0.
Second function does not include 0 in the permutations.
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