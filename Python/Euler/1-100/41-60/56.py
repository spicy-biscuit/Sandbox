"""
56: Powerful Digit Sum
"""

def SumOfDigits(N):
  Out = 0
  N = str(N)
  for x in range(len(N)):
    Out += int(N[x])
  return(Out)

Max = 0
for a in range(1, 100):
    for b in range(1, 100):
        c = a ** b
        c = SumOfDigits(c)
        if c > Max:
           Max = c

print(Max)