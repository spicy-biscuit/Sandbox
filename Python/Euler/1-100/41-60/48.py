"""
48: Self Powers
"""

def AddMod(A, B):
    return((A + B) % (10 ** 10))

def MultiplyMod(A, B):
    return((A * B) % (10 ** 10))

def PowerMod(A, B):
    Out = 1
    for x in range(B):
        Out = MultiplyMod(Out, A)
    return(Out)

Out = 0
for x in range(1, 1000 + 1):
    Out = AddMod(Out, PowerMod(x, x))

Out = str(Out)
while True:
    if len(Out) != 10:
        Out = "0" + Out
    else:
        break
print(Out)