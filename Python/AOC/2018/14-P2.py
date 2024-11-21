Input = 330121

Input = 51589
Input = 15891
# Input = '01245'
# Input = 92510
# Input = 59414

Input = str(Input)
List = []
for x in range(len(Input)):
  List.append(int(Input[x]))
Input = List
print(Input)

Recipes = [3, 7]

FirstIndex = 0
SecondIndex = 1

while True:
  if len(Recipes) % 1000000 == 0 or len(Recipes) % 1000000 == 1:
    print(len(Recipes))
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

  Subtract = 0
  if Recipes[-1 * len(Input):] == Input:
    print('0')
    break
  if Recipes[-1 * len(Input) - 1:-1] == Input:
    Subtract = 1
    print('1')
    break

print(len(Recipes) - len(Input) - Subtract)