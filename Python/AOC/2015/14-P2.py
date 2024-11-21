Input = ["""Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds."""]

Input = Input[0].split("\n")

AllReindeer = ["" for x in range(len(Input))]
Data = [0 for x in range(len(Input))]
Time = [0 for x in range(len(Input))]
Rest = [0 for x in range(len(Input))]
Distance = [0 for x in range(len(Input))]
Points = [0 for x in range(len(Input))]

for Info in Input:
  AllReindeer[Input.index(Info)] = Info[:Info.find(" ")]
  Speed1 = int(Info[Info.find("fly") + 4:Info.find("km/s") - 1])
  Time1 = int(Info[Info.find("for") + 4:Info.find("seconds") - 1])
  Rest1 = int(Info[Info.find("rest for") + 9:Info.find("seconds.") - 1])
  Data[Input.index(Info)] = [Speed1, Time1, Rest1]

for Index in range(len(AllReindeer)):
  Time[Index] = Data[Index][1]

for Second in range(2503):
  for Index in range(len(AllReindeer)):
    if Rest[Index] >= 2:
      Rest[Index] = Rest[Index] - 1
      continue
    if Time[Index] == 0:
      Rest[Index] = Data[Index][2]
      Time[Index] = Data[Index][1]
      continue
    Time[Index] = Time[Index] - 1
    Distance[Index] = Distance[Index] + Data[Index][0]
  MaxDistance = 0
  for Thing in Distance:
    if Thing > MaxDistance:
      MaxDistance = Thing
  for Index in range(len(AllReindeer)):
    if Distance[Index] == MaxDistance:
      Points[Index] = Points[Index] + 1
  print(Points)
print(max(Points))