Input = ["""Time:        56     97     77     93
Distance:   499   2210   1097   1440"""]
Input = Input[0]
Input = Input.split("\n")

Times = Input[0].split()[1:]
Distances = Input[1].split()[1:]

print(Times, Distances)

Product = 1
for RACE in range(len(Times)):
  Val = 0
  for TIME in range(int(Times[RACE])):
    RaceTime = int(Times[RACE])
    if TIME * (RaceTime - TIME) > int(Distances[RACE]):
      Val = (RaceTime - TIME) - (TIME) + 1
      break
  Product = Product * Val
  print(Product, Val)