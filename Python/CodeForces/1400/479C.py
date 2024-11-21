"""
479C: Exams
"""

N = int(input())

List = []

for x in range(N):
  List.append(tuple(map(int, input().split())))

# print(List)

def SortFunc1(tuple):
  return(tuple[1])
def SortFunc2(tuple):
  return(tuple[0])

List.sort(key=SortFunc1)
List.sort(key=SortFunc2)

# print(List)

Earliest = 0
for x in List:
  B = x[1]
  A = x[0]
  if B >= Earliest:
    Earliest = B
  else:
    Earliest = A
print(Earliest)

"""
ACCEPTED!
"""