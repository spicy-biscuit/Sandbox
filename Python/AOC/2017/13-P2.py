Input = ["""0: 4
1: 2
2: 3
4: 4
6: 8
8: 5
10: 6
12: 6
14: 10
16: 8
18: 6
20: 9
22: 8
24: 6
26: 8
28: 8
30: 12
32: 12
34: 12
36: 12
38: 10
40: 12
42: 12
44: 14
46: 8
48: 14
50: 12
52: 14
54: 14
58: 14
60: 12
62: 14
64: 14
66: 12
68: 12
72: 14
74: 18
76: 17
86: 14
88: 20
92: 14
94: 14
96: 18
98: 18"""]

# Input = ["""0: 3
# 1: 2
# 4: 4
# 6: 4"""]

Input = Input[0].split("\n")

Maximum = int(Input[-1][:Input[-1].find(" ") - 1])

Firewall = [[] for x in range(Maximum + 1)]

for x in Input:
  Index = int(x[:x.find(" ") - 1])
  Depth = int(x[x.find(" ") + 1:]) - 1
  Firewall[Index] = [0, Depth, "Out"]
  #[Current, Depth, in or out]

print(Firewall)

def Update():
  for Index in range(Maximum + 1):
    CurrentLayer = Firewall[Index]
    if CurrentLayer == []:
      continue
    if CurrentLayer[0] == CurrentLayer[1]:
      CurrentLayer[2] = "In"
    elif CurrentLayer[0] == 0:
      CurrentLayer[2] = "Out"
      
    if CurrentLayer[2] == "Out":
      CurrentLayer[0] += 1
    else:
      CurrentLayer[0] -= 1

Triggered = [[] for x in range(Maximum + 1)]

Delay = -1
while True:
  Delay += 1
  
  Original = []
  for x in Firewall:
    NewList = []
    for y in x:
      NewList.append(y)
    Original.append(NewList)
  
  Total = []
  for CurrentPosition in range(Maximum + 1):
    if Firewall[CurrentPosition] == []:
      Update()
      continue
    if Firewall[CurrentPosition][0] == 0:
      Triggered[CurrentPosition].append(Delay)
    Update()

  Firewall = Original
  Update()

  if Delay >= 100:
    break
    
NewTriggered = []

for x in Triggered:
  if x == []:
    continue
  NewTriggered.append([x[0], x[1] - x[0]])

Delay = 0
while True:
  Delay += 1
  Good = True
  for x in NewTriggered:
    if Delay % x[1] == x[0]:
      Good = False
      break
  if Good:
    break
  if Delay % 10000 == 0:
    print(Delay)

print(Delay)
