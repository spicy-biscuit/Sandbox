"""
279B: Books
"""

Line1 = input()
Line2 = input()

# print("----------")

Line1 = list(map(int, Line1.split()))
Line2 = list(map(int, Line2.split()))

n = Line1[0]
t = Line1[1]

Books = Line2

Start = 0
End = 1

Max = 0
Out = 0
# print(Books)
while True:
  if End > n - 1:
    break
  if Start == 0 and End == 1:
    Sum = sum(Books[Start:End])
  if Sum > t:
    Start += 1
    Sum -= Books[Start - 1]
  else:
    End += 1
    Sum += Books[End - 1]
  # Sum = sum(Books[Start:End])
  ThisOut = End - Start
  # print()
  # print(Start, End, ThisOut, Sum, ThisOut > Out and Sum <= t)
  # print(Books[Start:End])
  if ThisOut > Out and Sum <= t:
    Out = ThisOut

if n == 1:
  if Books[0] <= t:
    Out = 1
  else:
    Out = 0

if Out >= n:
  Out = n
print(Out)

"""
ACCEPTED!
"""