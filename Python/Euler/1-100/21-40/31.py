"""
31: Coin Sums
"""

def Function(ThisCoin, SumSoFar):
    if SumSoFar < 0:
        return(0)
    if ThisCoin == 1:
        return(1)
    if ThisCoin == 2:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(1, SumSoFar - ThisCoin * x)
        return(Out)
    if ThisCoin == 5:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(2, SumSoFar - ThisCoin * x)
        return(Out)
    if ThisCoin == 10:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(5, SumSoFar - ThisCoin * x)
        return(Out)
    if ThisCoin == 20:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(10, SumSoFar - ThisCoin * x)
        return(Out)
    if ThisCoin == 50:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(20, SumSoFar - ThisCoin * x)
        return(Out)
    if ThisCoin == 100:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(50, SumSoFar - ThisCoin * x)
        return(Out)
    if ThisCoin == 200:
        Out = 0
        for x in range(0, SumSoFar // ThisCoin + 1):
            Out += Function(100, SumSoFar - ThisCoin * x)
        return(Out)
    
print(Function(200, 200))