"""
1324B: Pair of Topics
"""

N = int(input())
TeacherInterest = list(map(int, input().split()))
StudentInterest = list(map(int, input().split()))

Interest = []

for x in range(N):
  Interest.append(TeacherInterest[x] - StudentInterest[x])

def FindIndex(List, Number):
  #Find first number greater than or equal to the number
  Length = len(List)
  Low = 0
  High = Length
  while True:
    # print(Low, High)
    if High - Low <= 5:
      break
    Index = Low + (High - Low) // 2
    if Index == Low:
      Index += 1
    Consider = List[Index]
    if Consider < Number:
      Low = Index + 1
    elif Consider == Number:
      Low = Index
      High = Index + 1
    else:
      High = Index
  # print(Number, List[Low:])
  Out = N
  for ThisIndex in range(max(Low - 2, 0), min(Length, High + 1)):
    Consider = List[ThisIndex]
    if Consider >= Number:
      Out = ThisIndex
      break
  return(Out)

Interest.sort()
# print(Interest)

#[-2, -1, 0, 3, 5]


Total = 0
for x in range(N):
  Current = Interest[x]
  FindThisNum = -1 * Current + 1
  if Interest[-1] < FindThisNum:
    continue
  # elif Current > 0:
  #   Total += N - x - 1
  else:
    Index = FindIndex(Interest, FindThisNum)
    AddThis = N - Index

    # AddThis = min(AddThis, N - x - 1)
    # print("A", AddThis)

    if AddThis > N - x - 1:
      Total -= 1
    
    Total += AddThis

Total = int(Total / 2)
print(Total)