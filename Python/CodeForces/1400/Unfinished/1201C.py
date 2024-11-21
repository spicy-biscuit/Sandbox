"""
1201C: Maximum Median
"""

Line1 = list(map(int, input().split()))

N = Line1[0]
K = Line1[1]

Array = list(map(int, input().split()))

Array.sort()

for x in range(N - 1):
  if Array[x + 1] < Array[x]:
    print("broken bitch :/")

Array = tuple(Array)

Index = int((N - 1) / 2)

Array = Array[Index:]

# print(Array)

TotalSum = sum(Array) + K

Out = TotalSum // len(Array)

print(Out)