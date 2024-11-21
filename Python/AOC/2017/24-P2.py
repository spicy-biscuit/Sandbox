Input = ["""48/5
25/10
35/49
34/41
35/35
47/35
34/46
47/23
28/8
27/21
40/11
22/50
48/42
38/17
50/33
13/13
22/33
17/29
50/0
20/47
28/0
42/4
46/22
19/35
17/22
33/37
47/7
35/20
8/36
24/34
6/7
7/43
45/37
21/31
37/26
16/5
11/14
7/23
2/23
3/25
20/20
18/20
19/34
25/46
41/24
0/33
3/7
49/38
47/22
44/15
24/21
10/35
6/21
14/50"""]

# Input = ["""0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10"""]

Input = Input[0].split("\n")

def Function(Item):
  return(100000 * Item[1] + Item[0])

for Index in range(len(Input)):
  Input[Index] = Input[Index].split("/")
  Input[Index][0] = int(Input[Index][0])
  Input[Index][1] = int(Input[Index][1])
  Input[Index] = tuple(Input[Index])
  
for x in Input:
  print(x)

from functools import cache

@cache
def Bridge(CurrentStrength, LastPort, RemainingPieces, Length):
  NowhereLeft = True
  for Piece in RemainingPieces:
    if Piece[0] == LastPort or Piece[1] == LastPort:
      NowhereLeft = False
      break
  if NowhereLeft:
    return([CurrentStrength, Length])

  List = []
  for Piece in RemainingPieces:
    if Piece[0] == LastPort:
      NewPieces = RemainingPieces
      NewPieces = list(NewPieces)
      NewPieces.remove(Piece)
      NewPieces = tuple(NewPieces)
      List.append(Bridge(CurrentStrength + Piece[0] + Piece[1], Piece[1], NewPieces, Length + 1))
    if Piece[1] == LastPort:
      NewPieces = RemainingPieces
      NewPieces = list(NewPieces)
      NewPieces.remove(Piece)
      NewPieces = tuple(NewPieces)
      List.append(Bridge(CurrentStrength + Piece[0] + Piece[1], Piece[0], NewPieces, Length + 1))
  return(max(List, key=Function))

print(Bridge(0, 0, tuple(Input), 0))