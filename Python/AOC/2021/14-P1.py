Input = ["""OOFNFCBHCKBBVNHBNVCP

PH -> V
OK -> S
KK -> O
BV -> K
CV -> S
SV -> C
CK -> O
PC -> F
SC -> O
KC -> S
KF -> N
SN -> C
SF -> P
OS -> O
OP -> N
FS -> P
FV -> N
CP -> S
VS -> P
PB -> P
HP -> P
PK -> S
FC -> F
SB -> K
NC -> V
PP -> B
PN -> N
VN -> C
NV -> O
OV -> O
BS -> K
FP -> V
NK -> K
PO -> B
HF -> H
VK -> S
ON -> C
KH -> F
HO -> P
OO -> H
BC -> V
CS -> O
OC -> B
VB -> N
OF -> P
FK -> H
OH -> H
CF -> K
CC -> V
BK -> O
BH -> F
VV -> N
KS -> V
FO -> F
SH -> F
OB -> O
VH -> F
HH -> P
PF -> C
NF -> V
VP -> S
CN -> V
SK -> O
FB -> S
FN -> S
BF -> H
FF -> V
CB -> P
NN -> O
VC -> F
HK -> F
BO -> H
KO -> C
CH -> N
KP -> C
HS -> P
NP -> O
NS -> V
NB -> H
HN -> O
BP -> C
VF -> S
KN -> P
HC -> C
PS -> K
BB -> O
NO -> N
NH -> F
BN -> F
KV -> V
SS -> K
CO -> H
KB -> P
FH -> C
SP -> C
SO -> V
PV -> S
VO -> O
HV -> N
HB -> V"""]

# Input = ["""NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""]

Input = Input[0].split("\n\n")
Current = Input[0]
Instructions = Input[1].split("\n")

Pairs = []
Insert = []

for x in Instructions:
  x = x.split(" -> ")
  Pairs.append(x[0])
  Insert.append(x[1])

for Step in range(10):
  # print(Current)
  Indexes = []
  InsertThis = []
  for Index in range(len(Current) - 1):
    This = Current[Index:Index + 2]
    if This not in Pairs:
      continue
    ToInsert = Insert[Pairs.index(This)]
    Indexes.append(Index)
    InsertThis.append(ToInsert)
  Counter = -1
  for x in range(len(Indexes)):
    Counter += 1
    Index = Indexes[x] + Counter + 1
    ToInsert = InsertThis[x]
    Current = Current[:Index] + ToInsert + Current[Index:]
# print(Current)

List = [0 for x in range(26)]

for x in range(len(Current)):
  This = Current[x]
  This = ord(Current[x]) - 65
  List[This] += 1

Count = 0
for x in List:
  if x == 0:
    Count += 1
for x in range(Count):
  List.remove(0)

print(List)

print(max(List) - min(List))
