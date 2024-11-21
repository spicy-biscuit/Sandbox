"""
33: Digit Cancelling Fractions
"""

OutNum = 1
OutDen = 1
for Numerator in range(10, 100):
    for Denominator in range(Numerator + 1, 100):
        a = str(Numerator)
        b = str(Denominator)
        a = list(a)
        b = list(b)
        Common = ""
        for c in a:
            for d in b:
                if c == d:
                    Common = c
        if Common == "":
            continue
        a.remove(Common)
        b.remove(Common)
        if Common == "0":
            continue
        a = int(a[0])
        b = int(b[0])
        if b == 0:
            continue
        if a/b == Numerator / Denominator:
            # print(a, b, Numerator, Denominator)
            OutNum *= a
            OutDen *= b


print(OutNum, "/", OutDen)