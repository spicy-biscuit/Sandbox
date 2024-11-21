"""
Requires: N/A
Time Complexity: O(N) where N is length of the input
Memory Complexity: O(1)
Input Type: Integer
"""

def SumOfDigits(N):
    Out = 0
    N = str(N)
    for x in range(len(N)):
        Out += int(N[x])
    return(Out)
