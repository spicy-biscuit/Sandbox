"""
Requires: None
Time Complexity: O(sqrtN)
Memory Complexity: O(sqrtN)
Input Type: Integer
Output Type: List

Returns a list of all the prime factors of N.
"""

def PrimeFactors(N):
    List = []
    X = 1
    while True:
        X += 1
        if N == 1:
            return(List)
        if N % X == 0:
            List.append(X)
            while True:
                N //= X
                if N % X != 0:
                    break