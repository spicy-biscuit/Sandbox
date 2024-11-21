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
Amount = []

for x in Instructions:
  First = x[0] + x[6]
  Second = x[6] + x[1]
  x = x.split(" -> ")
  Pairs.append(x[0])
  Insert.append((First, Second))
  Amount.append(0)

Letters = []

for x in Instructions:
  if x[6] not in Letters:
    Letters.append(x[6])

LetterCount = [0 for x in range(len(Letters))]

for x in range(len(Current) - 1):
  Now = Current[x:x + 2]
  Amount[Pairs.index(Now)] += 1

print(Pairs)
print(Amount)

New = [0 for x in range(len(Pairs))]

for Step in range(40):
  New = [0 for x in range(len(Pairs))]
  for Pair in Pairs:
    InsertThese = Insert[Pairs.index(Pair)]
    # print(InsertThese)
    New[Pairs.index(InsertThese[0])] += 1 * Amount[Pairs.index(Pair)]
    New[Pairs.index(InsertThese[1])] += 1 * Amount[Pairs.index(Pair)]
  Amount = New
  print(Amount)

for x in range(len(Pairs)):
  ThisPair = Pairs[x]
  Multiplier = Amount[x] / 2
  First = ThisPair[0]
  Second = ThisPair[1]
  LetterCount[Letters.index(First)] += Multiplier
  LetterCount[Letters.index(Second)] += Multiplier
LetterCount[Letters.index(Current[0])] += 0.5
LetterCount[Letters.index(Current[-1])] += 0.5

print(LetterCount)
print(max(LetterCount) - min(LetterCount))
