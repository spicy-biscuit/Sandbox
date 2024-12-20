Input = ["""Sensor at x=13820, y=3995710: closest beacon is at x=1532002, y=3577287
Sensor at x=3286002, y=2959504: closest beacon is at x=3931431, y=2926694
Sensor at x=3654160, y=2649422: closest beacon is at x=3702627, y=2598480
Sensor at x=3702414, y=2602790: closest beacon is at x=3702627, y=2598480
Sensor at x=375280, y=2377181: closest beacon is at x=2120140, y=2591883
Sensor at x=3875726, y=2708666: closest beacon is at x=3931431, y=2926694
Sensor at x=3786107, y=2547075: closest beacon is at x=3702627, y=2598480
Sensor at x=2334266, y=3754737: closest beacon is at x=2707879, y=3424224
Sensor at x=1613400, y=1057722: closest beacon is at x=1686376, y=-104303
Sensor at x=3305964, y=2380628: closest beacon is at x=3702627, y=2598480
Sensor at x=1744420, y=3927424: closest beacon is at x=1532002, y=3577287
Sensor at x=3696849, y=2604845: closest beacon is at x=3702627, y=2598480
Sensor at x=2357787, y=401688: closest beacon is at x=1686376, y=-104303
Sensor at x=2127900, y=1984887: closest beacon is at x=2332340, y=2000000
Sensor at x=3705551, y=2604421: closest beacon is at x=3702627, y=2598480
Sensor at x=1783014, y=2978242: closest beacon is at x=2120140, y=2591883
Sensor at x=2536648, y=2910642: closest beacon is at x=2707879, y=3424224
Sensor at x=3999189, y=2989409: closest beacon is at x=3931431, y=2926694
Sensor at x=3939169, y=2382534: closest beacon is at x=3702627, y=2598480
Sensor at x=2792378, y=2002602: closest beacon is at x=2332340, y=2000000
Sensor at x=3520934, y=3617637: closest beacon is at x=2707879, y=3424224
Sensor at x=2614525, y=1628105: closest beacon is at x=2332340, y=2000000
Sensor at x=2828931, y=3996545: closest beacon is at x=2707879, y=3424224
Sensor at x=2184699, y=2161391: closest beacon is at x=2332340, y=2000000
Sensor at x=2272873, y=1816621: closest beacon is at x=2332340, y=2000000
Sensor at x=1630899, y=3675405: closest beacon is at x=1532002, y=3577287
Sensor at x=3683190, y=2619409: closest beacon is at x=3702627, y=2598480
Sensor at x=180960, y=185390: closest beacon is at x=187063, y=-1440697
Sensor at x=1528472, y=3321640: closest beacon is at x=1532002, y=3577287
Sensor at x=3993470, y=2905566: closest beacon is at x=3931431, y=2926694
Sensor at x=1684313, y=20931: closest beacon is at x=1686376, y=-104303
Sensor at x=2547761, y=2464195: closest beacon is at x=2120140, y=2591883
Sensor at x=3711518, y=845968: closest beacon is at x=3702627, y=2598480
Sensor at x=3925049, y=2897039: closest beacon is at x=3931431, y=2926694
Sensor at x=1590740, y=3586256: closest beacon is at x=1532002, y=3577287
Sensor at x=1033496, y=3762565: closest beacon is at x=1532002, y=3577287"""]

# Input = ["""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""]

Input = Input[0].split("\n")

List = []
for x in Input:
  x = x[x.find("at") + 3:]
  a = x[:x.find(":")]
  x = x[x.find("at") + 3:]
  a = a.split(", ")
  x = x.split(", ")
  a[0] = int(a[0][2:])
  a[1] = int(a[1][2:])
  x[0] = int(x[0][2:])
  x[1] = int(x[1][2:])
  List.append((a[0], a[1], x[0], x[1]))

# print(List)

Sensors = []
Beacons = []
for x in List:
  Sensors.append((x[0], x[1]))
  Beacons.append((x[2], x[3]))

for x in range(len(List)):
  Sensor = Sensors[x]
  Beacon = Beacons[x]
  Distance = abs(Beacon[0] - Sensor[0]) + abs(Beacon[1] - Sensor[1])
  Sensors[x] = Sensor + (Distance,)

def SortFunc(Tuple):
  return(1000000000 * Tuple[0] + Tuple[1])

def Union(AllTuples):
  # print(AllTuples)
  if len(AllTuples) == 1:
    return(AllTuples[0])
  Tuple1 = AllTuples[0]
  Tuple2 = AllTuples[1]
  
  Start1 = Tuple1[0]
  End1 = Tuple1[1]
  Start2 = Tuple2[0]
  End2 = Tuple2[1]

  if End1 < Start2 - 1 and len(AllTuples) == 2:
    return(AllTuples)

  if End1 < Start2 - 1:
    RealNew = Union([Tuple2] + AllTuples[2:])
    if type(RealNew) is tuple:
      RealNew = [RealNew]
    return(Union([Tuple1] + RealNew))

  New = (min(Start1, Start2), max(End1, End2))
  return(Union([New] + AllTuples[2:]))

for Y in range(4000000 + 1):
  if Y % 10000 == 0:
    print(Y)
  AllUnions = []
  for Sensor in Sensors:
    This = []
    YDif = abs(Y - Sensor[1])
    Width = Sensor[2] - YDif
    if Width <= 0:
      continue
    This = (Sensor[0] - Width, Sensor[0] + Width)
    AllUnions.append(This)
  AllUnions.sort(key=SortFunc)
  # print(AllUnions)
  AllUnions = Union(AllUnions)
  # print(AllUnions)
  if type(AllUnions) is list:
    print()
    print()
    print(AllUnions)
    X = AllUnions[0][1] + 1
    print(X, Y)
    print(4000000 * X + Y)
    Out = 4000000 * X + Y
    break

print(Out)
