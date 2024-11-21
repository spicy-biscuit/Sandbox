"""
Requires: None
Time Complexity: log(N)
Memory Complexity: log(N)
Input Type: Integer
Output Type: String
"""

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