"""
1348B: Phoenix and Beauty
"""

T = int(input())

for TestCase in range(T):
  In = list(map(int, input().split()))
  N = In[0]
  K = In[1]

  List = list(map(int, input().split()))

  Unique = []
  for x in List:
    if x not in Unique:
      Unique.append(x)
  # print(Unique)

  if K < len(Unique):
    print("-1")
    continue

  while True:
    if K > len(Unique):
      Unique.append(Unique[0])
    else:
      break

  AddThis = Unique.copy()
  while True:
    if len(Unique) != K * N:
      Unique = Unique + AddThis
    else:
      break

  print(len(Unique))
  Out = ""
  for x in Unique:
    Out = Out + str(x) + " "
  Out = Out[:-1]
  print(Out)

"""
ACCEPTED!
"""