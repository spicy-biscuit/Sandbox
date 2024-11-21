"""
66: Diophantine Equation
"""

import math

def AddFractions(Num1, Den1, Num2, Den2):
   Num1 = Num1 * Den2 + Num2 * Den1
   Den1 = Den1 * Den2
#    Out = Reduce(Num1, Den2)
   Out = [Num1, Den2]
   return(Out)

def GetValueN(N, xth):

    if round(math.sqrt(N)) ** 2 == N:
        return(0)

    Set = []

    Current = (math.floor(math.sqrt(N)), 1, N, math.floor(math.sqrt(N)))
    #(a, b, c, d) means:
    # a, b/(sqrt(c) - d)
    Counter = 0
    while True:
        # print(Current)
        if Counter == xth:
            return(Current[0])
        Counter += 1
        Set.append(Current)

        a = Current[0]
        b = Current[1]
        c = Current[2]
        d = Current[3]

        e = math.sqrt(c) + d
        f = (c-d**2)//b

        g = e/f

        Adder = 0
        while True:
            if g > 1:
                g -= 1
                Adder += 1
                continue
            break

        Current = (Adder, f, c, Adder * f - d)

def calculateN(InputNum, N):
    N += 1
    List = [GetValueN(InputNum, x) for x in reversed(range(1, N))]
    Fraction = [1, List[0]]
    List = List[1:]
    for x in List:
        # print(Fraction)
        Fraction = AddFractions(x, 1, Fraction[0], Fraction[1])
        Fraction = [Fraction[1], Fraction[0]]
    # Fraction = AddFractions(1, 1, Fraction[0], Fraction[1])

    Fraction = [Fraction[1], Fraction[0]]

    Fraction = [Fraction[1] + (math.floor(math.sqrt(InputNum))) * Fraction[0], Fraction[0]]

    return(Fraction)

def SquareCheck(N):
    if abs(round(N) - N) > 0.0000005:
        return(False)
    x = round(math.sqrt(N))
    if x ** 2 == N:
        return(True)
    return(False)

def MinXSolution(D):
    if D == 0:
        return(0)
    X = 0
    while True:
        X += 1
        List = calculateN(D, X)
        x = List[0]
        y = List[1]
        # print(x, y, x**2 - D * (y**2))
        if x ** 2 - D * (y ** 2) == 1:
            return(x)
        
MaxOut = 0
RealOut = 0

# print(MinXSolution(2))
# print(MinXSolution(3))
# print(MinXSolution(5))
# print(MinXSolution(6))
# print(MinXSolution(7))
# print(MinXSolution(61))

for D in range(2, 1000 + 1):
    if SquareCheck(D):
        continue
    MinSolution = MinXSolution(D)
    # print(D, MinSolution)
    if MinSolution > MaxOut:
        MaxOut = MinSolution
        RealOut = D
        print(RealOut, MaxOut)
print(RealOut)