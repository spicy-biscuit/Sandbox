"""
5: Smallest Multiple
"""

def PrimeDivisors(N):
  List = []
  i = 2
  while True:
    if N == 1:
      break
    if N % i == 0:
      N //= i
      List.append(i)
    else:
      i += 1
  return(List)

def LCM(a, b):
  A = PrimeDivisors(a)
  B = PrimeDivisors(b)
  New = []
  for x in A:
    New.append(x)
    if x in B:
      B.remove(x)
  for x in B:
    New.append(x)
  Out = 1
  for x in New:
    Out *= x
  return(Out)

Out = 1
for x in range(1, 21):
  Out = LCM(Out, x)
print(Out)