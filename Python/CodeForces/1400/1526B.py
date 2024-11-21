"""
1526B: I Hate 1111
"""

N = int(input())

List = []

for x in range(N):
  List.append(int(input()))

# print(List)

def IsValid(Number):
  if Number % 11 == 0:
    return(True)
  if Number < 111:
    return(False)
  return(IsValid(Number - 111))

for x in List:
  if IsValid(x):
    print("YES")
  else:
    print("NO")

"""
ACCEPTED!
"""