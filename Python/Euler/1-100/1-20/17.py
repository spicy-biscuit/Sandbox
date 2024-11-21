"""
17: Number Letter Counts
"""

def Count(N):
  if N == 1000:
    return(11)
  if N < 10:
    if N == 0:
      return(0)
    if N in [1, 2, 6]:
      return(3)
    if N in [4, 5, 9]:
      return(4)
    if N in [3, 7, 8]:
      return(5)
  if N < 20:
    if N == 10:
      return(3)
    if N in [11, 12]:
      return(6)
    if N in [15, 16]:
      return(7)
    if N in [13, 14, 18, 19]:
      return(8)
    if N in [17]:
      return(9)
  if N < 100:
    if N < 30:
      return(6 + Count(N - 20))
    if N < 40:
      return(6 + Count(N - 30))
    if N < 50:
      return(5 + Count(N - 40))
    if N < 60:
      return(5 + Count(N - 50))
    if N < 70:
      return(5 + Count(N - 60))
    if N < 80:
      return(7 + Count(N - 70))
    if N < 90:
      return(6 + Count(N - 80))
    if N < 100:
      return(6 + Count(N - 90))

  HundredsPlace = (N - N % 100) // 100
  Int = N % 100
  if Int == 0:
    return(Count(HundredsPlace) + 7)
  return(Count(HundredsPlace) + 10 + Count(Int))

Out = 0
for x in range(1, 1000 + 1):
  Out += (Count(x))
print(Out)