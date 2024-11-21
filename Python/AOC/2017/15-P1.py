Input = ["""Generator A starts with 512
Generator B starts with 191"""]
InputA = 512
InputB = 191

# InputA = 65 #samples
# InputB = 8921

from functools import cache

# @cache
def Modulo(Number):
  return(Number % (2 ** 16))

# @cache
# def Binary(Number):
#   String = ""
#   for x in reversed(range(16)):
#     if Number >= 2 ** x:
#       Number -= 2 ** x
#       String = String + "1"
#     else:
#       String = String + "0"
#   return(String)

# @cache
# def Check(A, B):
#   if Modulo(A) == Modulo(B):
#     return(True)
#   return(False)

Old = 0
All = []
OriginalA = InputA
OriginalB = InputB
Count = 0
for Cycle in range(1, 40000001):
  InputA = (InputA * 16807) % 2147483647
  InputB = (InputB * 48271) % 2147483647
  if Modulo(InputA) == Modulo(InputB):
    Count += 1
    print(Count, Cycle, Cycle - Old)
    Old = Cycle

print(Count)
