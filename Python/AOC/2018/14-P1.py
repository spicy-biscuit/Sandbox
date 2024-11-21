Input = 330121

# Input = 9
# Input = 5
# Input = 18
# Input = 2018

Recipes = [3, 7]

FirstIndex = 0
SecondIndex = 1

while True:
  if len(Recipes) >= Input + 20:
    break

  Sum = Recipes[FirstIndex] + Recipes[SecondIndex]
  if Sum < 10:
    Recipes.append(Sum)
  else:
    Recipes.append(1)
    Recipes.append(Sum - 10)

  FirstIndex += Recipes[FirstIndex] + 1
  SecondIndex += Recipes[SecondIndex] + 1
  FirstIndex %= len(Recipes)
  SecondIndex %= len(Recipes)

String = ""
for x in (Recipes[Input:Input+10]):
  String += str(x)
print(String)
