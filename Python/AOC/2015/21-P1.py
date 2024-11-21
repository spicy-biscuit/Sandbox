Input = ["""Hit Points: 100
Damage: 8
Armor: 2"""]

Shop = ["""Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""]

Shop = Shop[0].split("\n\n")
UnprocessedWeapons = Shop[0]
UnprocessedArmors = Shop[1]
UnprocessedRings = Shop[2]

Weapons = []
Armors = []
Rings = []

UnprocessedWeapons = UnprocessedWeapons.split("\n")[1:]
UnprocessedArmors = UnprocessedArmors.split("\n")[1:]
UnprocessedRings = UnprocessedRings.split("\n")[1:]

for Line in UnprocessedWeapons:
  Line = Line.split()[1:]
  for x in range(len(Line)):
    Line[x] = int(Line[x])
  Weapons.append(Line)

for Line in UnprocessedArmors:
  Line = Line.split()[1:]
  for x in range(len(Line)):
    Line[x] = int(Line[x])
  Armors.append(Line)

for Line in UnprocessedRings:
  Line = Line.split()[2:]
  for x in range(len(Line)):
    Line[x] = int(Line[x])
  Rings.append(Line)

Armors = [[0, 0, 0]] + Armors
Rings = [[0, 0, 0]] + Rings


Input = Input[0].split("\n")

for x in range(3):
  Input[x] = Input[x][Input[x].find(":") + 2:]
  Input[x] = int(Input[x])

BossStats = Input

def Fight(Health, Attack, Defense, BossHealth):
  BossHealth = BossHealth - (Attack - BossStats[2])
  if BossHealth <= 0:
    return("Win")
  Health = Health - (BossStats[1] - Defense)
  if Health <= 0:
    return("Lose")
  return(Fight(Health, Attack, Defense, BossHealth))

MinCost = float('inf')
for Weapon in Weapons:
  for Armor in Armors:
    for Ring1 in Rings:
      for Ring2 in Rings:
        if Ring1 == Ring2 and Ring1 != [0, 0, 0]:
          continue
        RealQualities = [0, 0, 0]
        for x in range(3):
          RealQualities[x] = Weapon[x] + Armor[x] + Ring1[x] + Ring2[x]
        Cost = RealQualities[0]
        Attack = RealQualities[1]
        Defense = RealQualities[2]
        if Fight(100, Attack, Defense, BossStats[0]) == "Win" and Cost < MinCost:
          MinCost = Cost
          print(Cost)