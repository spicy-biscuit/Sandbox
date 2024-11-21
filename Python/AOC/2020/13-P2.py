Input = ["""1000390
13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"""]

# Input = ["""1
# 1789,37,47,1889"""]

Input = Input[0].split("\n")

List = Input[1].split(',')
Buses = []
Offsets = []
Offset = -1
for x in List:
  Offset += 1
  if x != "x":
    Buses.append(int(x))
    Offsets.append(Offset)

# print(Buses)
# print(Offsets)

RemainingBuses = []
RemainingOffsets = []
for x in Buses:
  RemainingBuses.append(x)
for x in Offsets:
  RemainingOffsets.append(x)

Adder = 1

TimeStamp = 0
while True:
  if len(RemainingBuses) == 0:
    break
  TimeStamp += Adder
  for Bus in RemainingBuses:
    Index = RemainingBuses.index(Bus)
    Offset = RemainingOffsets[Index]
    # print(TimeStamp, Offset, Bus)
    if (TimeStamp + Offset) % Bus == 0:
      # print("yes")
      RemainingBuses.remove(Bus)
      RemainingOffsets.remove(Offset)
      Adder *= Bus
    # else:
    #   print("no")
  # print(TimeStamp)


print(TimeStamp)
  