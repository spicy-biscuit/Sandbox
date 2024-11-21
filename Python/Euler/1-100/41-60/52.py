"""
52: Permuted Multiples
"""

def CheckAgainst(Num1, Num2):
    Num1 = list(str(Num1))
    Num2 = list(str(Num2))
    Num1.sort()
    Num2.sort()
    if Num1 == Num2:
        return(True)
    return(False)

def CheckAll(List):
    for x in range(len(List) - 1):
        if CheckAgainst(List[x], List[x + 1]) == False:
            return(False)
    return(True)
    
Current = 0
while True:
    Current += 1
    # print(Current)
    All = [Current * x for x in range(1, 7)]
    if CheckAll(All):
        print(Current)
        break