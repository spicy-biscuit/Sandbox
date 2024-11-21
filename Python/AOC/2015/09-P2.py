Input = ["""Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70"""]

Input = Input[0].split("\n")

Cities = []

for x in Input:
  City = x[:x.find(" to ")]
  if City not in Cities:
    Cities.append(City)
  City = x[x.find(" to ") + 4:x.find("=") - 1]
  if City not in Cities:
    Cities.append(City)
print(Cities)

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

Distances = [[0 for x in range(len(Cities))] for y in range(len(Cities))]

for Item in Input:
  City1 = Item[:Item.find(" to ")]
  City2 = Item[Item.find(" to ") + 4:Item.find("=") - 1]
  Distance = int(Item[Item.find("=") + 2:])
  Distances[Cities.index(City1)][Cities.index(City2)] = Distance
  Distances[Cities.index(City2)][Cities.index(City1)] = Distance
for x in Distances:
  print(x)

MaxDistance = 0
for Path in AllPermutations(len(Cities)):
  Total = 0
  for x in range(len(Cities) - 1):
    City1Index = int(Path[x])
    City2Index = int(Path[x + 1])
    Distance = Distances[City1Index][City2Index]
    Total += Distance
  if Total > MaxDistance:
    MaxDistance = Total
    print(Total, Path)
    