"""
Requires: None
Time Complexity: O(N) where N is the length of the string
Memory Complexity: O(1)
Input Type: String or Integer
"""

def IsPalindrome(N):
    N = str(N)
    if N == N[::-1]:
        return(True)
    return(False)