"""
1347D: Zero Remainder Array
"""

T = int(input())

for Testcase in range(T):
  # print("Input:")
  Line1 = list(map(int, input().split()))
  N = Line1[0]
  K = Line1[1]

  def Modulus(Input):
    return(Input % K)
    
  # Array = list(map(int, input().split()))
  
  # print("---------")
  # print("Output:")
  
  # New = list(map(Modulus, list(map(int, input().split()))))

  # Array = [0 for x in range(K)]

  IndexingSet = set([])
  Array = dict([])

  Max = 0
  # IndexOfMax = -1
  for x in list(map(Modulus, list(map(int, input().split())))):
    if x == 0:
      continue
    if x in IndexingSet:
      Array[x] = Array[x] + 1
      if Array[x] > Max:
        Max = Array[x]
      #   IndexOfMax = Index
    else:
      IndexingSet.add(x)
      Array[x] = 1
      if Array[x] > Max:
        Max = Array[x]

  # Array.reverse()

  if len(Array) == 0:
    print("0")
    continue

  # print("-----")
  # print(Array)
  # print(Indexing)
  # print("------")

  # Max = max(Array)
  if Max == 0:
    print("0")
    # Array.clear()
    # New.clear()
    # print()
    # print()
    continue
  # Index = Indexing[Array.index(Max)]
  # RealIndex = float('inf')
  # for x in range(len(Indexing)):
  #   if Array[x] == Max:
  #     if Indexing[x] < RealIndex:
  #       RealIndex = Indexing[x]

  RealIndex = float('inf')
  for x in IndexingSet:
    if Array[x] == Max:
      if x < RealIndex:
        RealIndex = x
  # print(RealIndex)
  Index = RealIndex
  Index = K - Index
  print((Max - 1) * K + Index + 1)
  # Array.clear()
  # Indexing.clear()
  # New.clear()
  
  # print(Array)
  # print()
  # print()

"""
ACCEPTED!
"""

"""
Notes:
>Use dictionaries
  >Dumbass
"""