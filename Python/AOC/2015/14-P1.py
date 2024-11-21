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

def FindDistance(Speeds, Seconds):
  TotalDistance = 0
  Speed = Speeds[0]
  OriginalTime = Speeds[1]
  OriginalRest = Speeds[2]

  Time = OriginalTime
  Rest = 0
  for Second in range(Seconds):
    if Rest >= 2:
      Rest -= 1
      continue
    if Time == 0:
      Rest = OriginalRest
      Time = OriginalTime
      continue
    Time -= 1
    TotalDistance += Speed
  return(TotalDistance)

AllReindeer = ["" for x in range(len(Input))]
Data = [0 for x in range(len(Input))]

print(FindDistance([14, 10, 127], 1000))
print(FindDistance([16, 11, 162], 1000))

for Info in Input:
  AllReindeer[Input.index(Info)] = Info[:Info.find(" ")]
  Speed = int(Info[Info.find("fly") + 4:Info.find("km/s") - 1])
  Time = int(Info[Info.find("for") + 4:Info.find("seconds") - 1])
  Rest = int(Info[Info.find("rest for") + 9:Info.find("seconds.") - 1])
  print(Speed, Time, Rest)
  Data[Input.index(Info)] = [Speed, Time, Rest]

MaxDistance = 0
for Index in range(len(AllReindeer)):
  print(AllReindeer[Index], FindDistance(Data[Index], 2503))
  if FindDistance(Data[Index], 2503) > MaxDistance:
    MaxDistance = FindDistance(Data[Index], 2503)
print("Max distance: " + str(MaxDistance))
  