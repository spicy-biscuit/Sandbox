"""
38: Concatenated Multiples
"""

def IsPandigital(N):
    N = str(N)
    if len(N) != 9:
        return(False)
    N = list(N)
    N.sort()
    return(N == [str(x) for x in range(1, 10)])

Max = 0
for x in range(1, 10000):
    String = ""
    Multipler = 0
    while True:
        Multipler += 1
        String = String + str(x * Multipler)
        if len(String) >= 9:
            break
    if IsPandigital(String):
        String = int(String)
        if String > Max:
            Max = String

print(Max)