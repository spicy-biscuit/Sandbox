Input = ["""Time:        56     97     77     93
Distance:   499   2210   1097   1440"""]
Input = Input[0]
Input = Input.split("\n")

Times = Input[0].split()[1:]
Distances = Input[1].split()[1:]

print(Times, Distances)

RealTime = ""
RealDistance = ""
for x in range(len(Times)):
  RealTime = RealTime + Times[x]
  RealDistance = RealDistance + Distances[x]

for TIME in range(int(RealTime)):
  RaceTime = int(RealTime)
  if TIME * (RaceTime - TIME) > int(RealDistance):
    Val = (RaceTime - TIME) - (TIME) + 1
    break
print(Val)