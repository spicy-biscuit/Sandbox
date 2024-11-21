import os

os.system('clear')
while True:
  print("How many dice should be rolled?")
  Dice = input("")
  if Dice.isdigit() == False:
    os.system('clear')
    print("Please give a number.")
    continue
  if Dice.count(".") != 0:
    os.system('clear')
    print("Please give an integer.")
    continue
  Dice = int(Dice)
  if Dice <= 0:
    os.system('clear')
    print("Please give a positive number.")
    continue
  else:
    break
print()
while True:
  print("How large should the total be?")
  Total = input("")
  if Total.isdigit() == False:
    os.system('clear')
    print("Please give a number.")
    continue
  if Total.count(".") != 0:
    os.system('clear')
    print("Please give an integer.")
    continue
  Total = int(Total)
  if Total <= 0:
    os.system('clear')
    print("Please give a positive number.")
    continue
  else:
    break

OGDice = Dice

List = [0 for x in range(Total+1)]
List[-1] = 1
SecondList = [0 for x in range(Total+1)]

while Dice != 1:
  Dice -= 1
  for x in range(len(List)):
    for y in range(1, 7):
      if x - y < 0:
        break
      SecondList[x-y] = SecondList[x-y] + List[x]
  List = SecondList
  SecondList = [0 for x in range(Total+1)]

Out = List[1] + List[2] + List[3] + List[4] + List[5] + List[6]

print("There are " + str(Out) + " possible ways to roll " + str(Total) + " with " + str(OGDice) + " dice.")