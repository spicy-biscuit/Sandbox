Input = ["""108, 324
46, 91
356, 216
209, 169
170, 331
332, 215
217, 104
75, 153
110, 207
185, 102
61, 273
233, 301
278, 151
333, 349
236, 249
93, 155
186, 321
203, 138
103, 292
47, 178
178, 212
253, 174
348, 272
83, 65
264, 227
239, 52
243, 61
290, 325
135, 96
165, 339
236, 132
84, 185
94, 248
164, 82
325, 202
345, 323
45, 42
292, 214
349, 148
80, 180
314, 335
210, 264
302, 108
235, 273
253, 170
150, 303
249, 279
255, 159
273, 356
275, 244"""]

# Input = ["""1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""]

Input = Input[0].split("\n")

for x in range(len(Input)):
  Input[x] = Input[x].split(', ')
  Input[x][0] = int(Input[x][0])
  Input[x][1] = int(Input[x][1])
  Input[x] = tuple(Input[x])
Input = tuple(Input)

for x in Input:
  print(x)

def FindClosestPoint(ThisPoint, AllPoints):
  MinimumDistance = float('inf')
  All = ([])
  Index = -1
  for Point in AllPoints:
    Index += 1
    Distance = abs(Point[1] - ThisPoint[1]) + abs(Point[0] - ThisPoint[0])
    # print(Distance, MinimumDistance)
    if Distance < MinimumDistance:
      All = ([Index])
      MinimumDistance = Distance
    elif Distance == MinimumDistance:
      All.append(Index)
  return(All)

Infinities = ([])
for x in range(-1000, 1000):
  ThisOne = FindClosestPoint((x, -1000), Input)
  if len(ThisOne) == 1:
    if ThisOne[0] not in Infinities:
      Infinities.append(ThisOne[0])
  ThisOne = FindClosestPoint((x, 1000), Input)
  if len(ThisOne) == 1:
    if ThisOne[0] not in Infinities:
      Infinities.append(ThisOne[0])
  ThisOne = FindClosestPoint((-1000, x), Input)
  if len(ThisOne) == 1:
    if ThisOne[0] not in Infinities:
      Infinities.append(ThisOne[0])
  ThisOne = FindClosestPoint((1000, x), Input)
  if len(ThisOne) == 1:
    if ThisOne[0] not in Infinities:
      Infinities.append(ThisOne[0])

print(Infinities)

Totals = [0 for x in range(len(Input))]
for Row in range(-100, 600):
  for Column in range(-100, 600):
    ThisOne = FindClosestPoint((Row, Column), Input)
    if len(ThisOne) == 1:
      Totals[ThisOne[0]] += 1

for Index in range(len(Totals)):
  if Index in Infinities:
    Totals[Index] = 0
print(max(Totals))
    