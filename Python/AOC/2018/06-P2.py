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

def TotalDistance(ThisPoint, AllPoints):
  TotalDistance = 0
  for x in AllPoints:
    TotalDistance += abs(x[0] - ThisPoint[0]) + abs(x[1] - ThisPoint[1])
  return(TotalDistance)

Total = 0
for Row in range(-200, 500):
  for Column in range(-200, 500):
    if TotalDistance((Row, Column), Input) < 10000:
      Total += 1
print(Total)
