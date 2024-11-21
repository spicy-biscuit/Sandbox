"""
26: Reciprocal Cycles
"""

def FindDecimal(N):
    Decimals = []
    Remaining = 1
    Index = -1
    Seen = []
    while True:
        if (Remaining, N) in Seen:
            Seen.reverse()
            return(Seen.index((Remaining, N)) + 1)
            break
        Seen.append((Remaining, N))
        Index += 1
        if Remaining < N:
            Decimals.append(0)
            Remaining *= 10
            continue
        Decimals.append(Remaining // N)
        Remaining -= (Remaining // N) * N
        Remaining *= 10
        continue

# print(FindDecimal(243))

Max = 0
Out = 0
for x in range(2, 1000):
    This = (FindDecimal(x))
    if This > Max:
        Max = This
        Out = x
print(Out)