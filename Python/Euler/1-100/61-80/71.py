"""
71: Ordered Fractions
"""

def SortFunc(Fraction):
    return(Fraction[0] / Fraction[1])

n = 0
d = 1
Best = [0, 1]

from fractions import Fraction

while d <= 1000000:
    if d % 10000 == 0:
        print(d)
    if n/d < 3/7:
        n += 1
    else:
        d += 1
    
    # New = ReduceFraction([n, d])
    # q = Fraction(n, d)
    # New = [q.numerator, q.denominator]
    New = [n, d]

    if SortFunc(Best) < SortFunc(New) and SortFunc(New) < 3/7:
        Best = New

print(Best)
    