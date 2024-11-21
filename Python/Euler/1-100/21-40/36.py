"""
36: Double-Base Palindromes
"""

def IsPalindrome(N):
    N = str(N)
    if N == N[::-1]:
        return(True)
    return(False)

def DecimalToBinary(N):
    OutLength = 1
    while True:
        if 2 ** OutLength > N:
            break
        OutLength += 1
    String = ""
    for x in range(OutLength):
        y = 2 ** (OutLength - x - 1)
        if y <= N:
            N -= y
            String = String + "1"
        else:
            String = String + "0"
    return(String)


Out = 0
for x in range(1, 1000000):
    if IsPalindrome(x) and IsPalindrome(DecimalToBinary(x)):
        Out += x
print(Out)

