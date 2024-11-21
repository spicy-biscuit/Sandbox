Input = ["""Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""]

Input = Input[0].split("\n")

AllQualities = []

for Ingredient in Input:
  Ingredient = Ingredient[Ingredient.find(":") + 2:]
  Qualities = Ingredient.split(", ")
  for Index in range(len(Qualities)):
    Qualities[Index] = int(Qualities[Index][Qualities[Index].find(" ") + 1:])
  AllQualities.append(Qualities)

MaxScore = 0
for Sprinkles in range(101):
  for PeanutButter in range(101 - Sprinkles):
    for Frosting in range(101 - Sprinkles - PeanutButter):
      Sugar = 100 - Sprinkles - PeanutButter - Frosting
      Final = [0 for x in range(len(AllQualities[0]))]
      for Index in range(len(Final)):
        Final[Index] = Final[Index] + Sprinkles * AllQualities[0][Index]
        Final[Index] = Final[Index] + PeanutButter * AllQualities[1][Index]
        Final[Index] = Final[Index] + Frosting * AllQualities[2][Index]
        Final[Index] = Final[Index] + Sugar * AllQualities[3][Index]
      Score = 1
      if Final[4] != 500:
        continue
      for Index in range(len(Final) - 1):
        if Final[Index] <= 0:
          Score = 0
        Score = Score * Final[Index]
      if Score > MaxScore:
        MaxScore = Score
        print(MaxScore, Sprinkles, PeanutButter,Frosting,Sugar, Final)
        