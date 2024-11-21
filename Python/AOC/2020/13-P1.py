Input = ["""1000390
13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"""]

Input = Input[0].split("\n")

Start = int(Input[0])
List = Input[1].split(',')
Buses = []
for x in List:
  if x != "x":
    Buses.append(int(x))

print(Buses)

TimeStamp = Start - 1
while True:
  TimeStamp += 1
  Breakout = False
  for x in Buses:
    if TimeStamp % x == 0:
      print(x * (TimeStamp - Start))
      Breakout = True
      break
  if Breakout:
    break