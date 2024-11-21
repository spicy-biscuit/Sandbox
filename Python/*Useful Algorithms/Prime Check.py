"""
Requires: Math module
Time Complexity: O(sqrt(N))
Memory Complexity: O(1)
Input Type: Integer
Output Type: Boolean

Returns True if N is a prime, and False if not.
"""

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