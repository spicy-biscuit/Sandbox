"""
515C: Drazil and Factorial
"""

n = int(input())
a = input()

List = []
ExtraFactors = []

for x in range(n):
  This = int(a[x])
  if This == 1:
    continue
  elif This == 2:
    List.append(2)
    continue
  elif This == 3:
    List.append(3)
    continue
  elif This == 4:
    List.append(3)
    ExtraFactors.append(2)
    ExtraFactors.append(2)
    continue
  elif This == 5:
    List.append(5)
    continue
  elif This == 6:
    List.append(5)
    ExtraFactors.append(2)
    ExtraFactors.append(3)
    continue
  elif This == 7:
    List.append(7)
    continue
  elif This == 8:
    List.append(7)
    ExtraFactors.append(2)
    ExtraFactors.append(2)
    ExtraFactors.append(2)
    continue
  elif This == 9:
    List.append(7)
    ExtraFactors.append(3)
    ExtraFactors.append(3)
    ExtraFactors.append(2)
    ExtraFactors.append(2)
    ExtraFactors.append(2)
    continue

ExtraFactors.sort(reverse=True)

# print(List)
# print(ExtraFactors)

while True:
  if 3 in ExtraFactors:
    if 2 in ExtraFactors:
      List.append(3)
      ExtraFactors.remove(3)
      ExtraFactors.remove(2)
    else:
      if 2 in List:
        List.append(3)
        List.remove(2)
        ExtraFactors.remove(3)
      elif 5 in List and 2 in ExtraFactors:
        List.append(6)
        List.remove(5)
        ExtraFactors.remove(3)
        ExtraFactors.remove(2)
      elif 8 in List and ExtraFactors.count(3) >= 2:
        List.append(9)
        List.remove(8)
        ExtraFactors.remove(3)
        ExtraFactors.remove(3)
    continue
  elif 2 in ExtraFactors:
    List.append(2)
    ExtraFactors.remove(2)
  else:
    break

# print(List, ExtraFactors)

List.sort(reverse=True)


Out = ""
for x in List:
  Out = Out + str(x)
print(Out)

"""
ACCEPTED
"""