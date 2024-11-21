Input = ["""Alice would lose 57 happiness units by sitting next to Bob.
Alice would lose 62 happiness units by sitting next to Carol.
Alice would lose 75 happiness units by sitting next to David.
Alice would gain 71 happiness units by sitting next to Eric.
Alice would lose 22 happiness units by sitting next to Frank.
Alice would lose 23 happiness units by sitting next to George.
Alice would lose 76 happiness units by sitting next to Mallory.
Bob would lose 14 happiness units by sitting next to Alice.
Bob would gain 48 happiness units by sitting next to Carol.
Bob would gain 89 happiness units by sitting next to David.
Bob would gain 86 happiness units by sitting next to Eric.
Bob would lose 2 happiness units by sitting next to Frank.
Bob would gain 27 happiness units by sitting next to George.
Bob would gain 19 happiness units by sitting next to Mallory.
Carol would gain 37 happiness units by sitting next to Alice.
Carol would gain 45 happiness units by sitting next to Bob.
Carol would gain 24 happiness units by sitting next to David.
Carol would gain 5 happiness units by sitting next to Eric.
Carol would lose 68 happiness units by sitting next to Frank.
Carol would lose 25 happiness units by sitting next to George.
Carol would gain 30 happiness units by sitting next to Mallory.
David would lose 51 happiness units by sitting next to Alice.
David would gain 34 happiness units by sitting next to Bob.
David would gain 99 happiness units by sitting next to Carol.
David would gain 91 happiness units by sitting next to Eric.
David would lose 38 happiness units by sitting next to Frank.
David would gain 60 happiness units by sitting next to George.
David would lose 63 happiness units by sitting next to Mallory.
Eric would gain 23 happiness units by sitting next to Alice.
Eric would lose 69 happiness units by sitting next to Bob.
Eric would lose 33 happiness units by sitting next to Carol.
Eric would lose 47 happiness units by sitting next to David.
Eric would gain 75 happiness units by sitting next to Frank.
Eric would gain 82 happiness units by sitting next to George.
Eric would gain 13 happiness units by sitting next to Mallory.
Frank would gain 77 happiness units by sitting next to Alice.
Frank would gain 27 happiness units by sitting next to Bob.
Frank would lose 87 happiness units by sitting next to Carol.
Frank would gain 74 happiness units by sitting next to David.
Frank would lose 41 happiness units by sitting next to Eric.
Frank would lose 99 happiness units by sitting next to George.
Frank would gain 26 happiness units by sitting next to Mallory.
George would lose 63 happiness units by sitting next to Alice.
George would lose 51 happiness units by sitting next to Bob.
George would lose 60 happiness units by sitting next to Carol.
George would gain 30 happiness units by sitting next to David.
George would lose 100 happiness units by sitting next to Eric.
George would lose 63 happiness units by sitting next to Frank.
George would gain 57 happiness units by sitting next to Mallory.
Mallory would lose 71 happiness units by sitting next to Alice.
Mallory would lose 28 happiness units by sitting next to Bob.
Mallory would lose 10 happiness units by sitting next to Carol.
Mallory would gain 44 happiness units by sitting next to David.
Mallory would gain 22 happiness units by sitting next to Eric.
Mallory would gain 79 happiness units by sitting next to Frank.
Mallory would lose 16 happiness units by sitting next to George."""]

Input = Input[0].split("\n")

def AllPermutations(n):
  if n == 1:
    return("0")
  List = AllPermutations(n - 1)
  Output = []
  AppendThis = str(n - 1)
  for Permutation in List:
    for x in range(len(Permutation)):
      Output.append(Permutation[:x] + AppendThis + Permutation[x:])
    Output.append(Permutation + AppendThis)
  return(Output)

Names = []
for x in Input:
  Name = x[:x.find(" ")]
  if Name not in Names:
    Names.append(Name)
print(Names)

Grid = [[0 for x in range(len(Names))] for y in range(len(Names))]
"""
Accessing the Grid
Grid[Person1][Person2] means:
Person 1 gains this much happiness from sitting next to Person 2
"""

for Info in Input:
  Person1 = Info[:Info.find(" ")]
  Person2 = Info[Info.find("to") + 3:-1]
  Person1Index = Names.index(Person1)
  Person2Index = Names.index(Person2)
  if Info.find("gain") != -1:
    Number = int(Info[Info.find("gain") + 5:Info.find("happiness") - 1])
    Grid[Person1Index][Person2Index] = Number
  else:
    Number = int(Info[Info.find("lose") + 5:Info.find("happiness") - 1])
    Grid[Person1Index][Person2Index] = -1 * Number
for x in Grid:
  print(x)

MaxHappiness = 0
for PossibleArrangement in AllPermutations(len(Names)):
  TotalHappiness = 0
  PossibleArrangement = PossibleArrangement + PossibleArrangement[0]
  for Index in range(len(PossibleArrangement) - 1):
    Person1Index = int(PossibleArrangement[Index])
    Person2Index = int(PossibleArrangement[Index + 1])
    TotalHappiness += Grid[Person1Index][Person2Index]
    TotalHappiness += Grid[Person2Index][Person1Index]
  if TotalHappiness > MaxHappiness:
    print(TotalHappiness)
    MaxHappiness = TotalHappiness
  

