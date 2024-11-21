Input = []
Output = []
Instructions = [3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,28,2,1008,7,10,2,4,17,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,59,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,81,1006,0,24,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,105,2,6,13,10,1006,0,5,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,134,2,1007,0,10,2,1102,20,10,2,1106,4,10,1,3,1,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,172,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,194,1,103,7,10,1006,0,3,1,4,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,228,2,109,0,10,1,101,17,10,1006,0,79,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,260,2,1008,16,10,1,1105,20,10,1,3,17,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,295,1,1002,16,10,101,1,9,9,1007,9,1081,10,1005,10,15,99,109,641,104,0,104,1,21101,387365733012,0,1,21102,1,336,0,1105,1,440,21102,937263735552,1,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,3451034715,1,1,21101,0,394,0,1105,1,440,21102,3224595675,1,1,21101,0,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337454440,1,21102,428,1,0,1105,1,440,21101,0,825460798308,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21102,1,40,2,21101,0,471,3,21101,461,0,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,1,0,466,109,-2,2105,1,0,0,109,4,2101,0,-1,503,1207,-3,0,10,1006,10,521,21101,0,0,-3,21202,-3,1,1,22102,1,-2,2,21101,1,0,3,21102,540,1,0,1105,1,545,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22102,1,-4,-4,1106,0,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,587,1,0,1105,1,545,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,606,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,22102,1,-1,1,21102,1,628,0,105,1,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]
Values = []
Indexes = []

Painted = [(0, 0)]
EverPainted = []
CurrentRow = 0
CurrentColumn = 0
Direction = "Up"

"""
To retrieve a value from indexes:

Value = Values[Indexes.index(Index)]

To update an index:

Values[Indexes.index(Index)] = NewValue

"""

for x in range(len(Instructions)):
  Values.append(Instructions[x])
  Indexes.append(x)

RealIndex = 0
RelativeBase = 0

def GetVal(Index, Mode, Relative):
  if Index + Relative not in Indexes:
    Indexes.append(Index + Relative)
    Values.append(0)
  if Mode == 0:
    if Index not in Indexes:
      Indexes.append(Index)
      Values.append(0)
    FakeIndex = Indexes.index(Index)
    FakeIndex = Values[FakeIndex]
    if FakeIndex not in Indexes:
      Indexes.append(FakeIndex)
      Values.append(0)
    FakeIndex = Indexes.index(FakeIndex)
    return(Values[FakeIndex])
  if Mode == 1:
    if Index not in Indexes:
      Indexes.append(Index)
      Values.append(0)
    FakeIndex = Indexes.index(Index)
    return(Values[FakeIndex])
  if Mode == 2:
    if Index not in Indexes:
      Indexes.append(Index)
      Values.append(0)
    FakeIndex = Indexes.index(Index)
    FakeIndex = Values[FakeIndex] + Relative
    if FakeIndex not in Indexes:
      Indexes.append(FakeIndex)
      Values.append(0)
    FakeIndex = Indexes.index(FakeIndex)
    return(Values[FakeIndex])

while True:
  # print(Values)
  if RealIndex not in Indexes:
    Indexes.append(RealIndex)
    Values.append(0)
  if RealIndex + RelativeBase not in Indexes:
    Indexes.append(RealIndex + RelativeBase)
    Values.append(0)
  ThisValue = Values[Indexes.index(RealIndex)]

  Opcode = ThisValue % 100
  # print(ThisValue, Opcode)

  if Opcode == 99:
    break

  Modes = []
  # print(ThisValue)
  Modes.append(int((ThisValue % 1000 - ThisValue % 100) / 100))
  Modes.append(int((ThisValue % 10000 - ThisValue % 1000) / 1000))
  Modes.append(int((ThisValue % 100000 - ThisValue % 10000) / 10000))
  # print(Modes)

  if Opcode == 1:
    ValueIndexToUpdate = Values[Indexes.index(RealIndex + 3)]
    if ValueIndexToUpdate not in Indexes:
      Indexes.append(ValueIndexToUpdate)
      Values.append(0)
    if ValueIndexToUpdate + RelativeBase not in Indexes:
      Indexes.append(ValueIndexToUpdate + RelativeBase)
      Values.append(0)
    if Modes[2] == 2:
      Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = GetVal(RealIndex + 1, Modes[0], RelativeBase) + GetVal(RealIndex + 2, Modes[1], RelativeBase)
    else:
      Values[Indexes.index(ValueIndexToUpdate)] = GetVal(RealIndex + 1, Modes[0], RelativeBase) + GetVal(RealIndex + 2, Modes[1], RelativeBase)
    RealIndex += 4
    continue

  if Opcode == 2:
    ValueIndexToUpdate = Values[Indexes.index(RealIndex + 3)]
    if ValueIndexToUpdate not in Indexes:
      Indexes.append(ValueIndexToUpdate)
      Values.append(0)
    if ValueIndexToUpdate + RelativeBase not in Indexes:
      Indexes.append(ValueIndexToUpdate + RelativeBase)
      Values.append(0)
    if Modes[2] == 2:
      Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = GetVal(RealIndex + 1, Modes[0], RelativeBase) * GetVal(RealIndex + 2, Modes[1], RelativeBase)
    else:
      Values[Indexes.index(ValueIndexToUpdate)] = GetVal(RealIndex + 1, Modes[0], RelativeBase) * GetVal(RealIndex + 2, Modes[1], RelativeBase)
    RealIndex += 4
    continue

  if Opcode == 3:
    if (CurrentRow, CurrentColumn) in Painted:
      Input = [1]
    else:
      Input = [0]
    ValueIndexToUpdate = Values[Indexes.index(RealIndex + 1)]
    if ValueIndexToUpdate not in Indexes:
      Indexes.append(ValueIndexToUpdate)
      Values.append(0)
    if ValueIndexToUpdate + RelativeBase not in Indexes:
      Indexes.append(ValueIndexToUpdate + RelativeBase)
      Values.append(0)
    if Modes[0] == 2:
      Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = Input[0]
    else:
      Values[Indexes.index(ValueIndexToUpdate)] = Input[0]
    Input = Input[1:]
    RealIndex += 2
    continue

  if Opcode == 4:
    Output.append(GetVal(RealIndex + 1, Modes[0], RelativeBase))
    # print(Output)
    if len(Output) == 2:
      Color = Output[0]
      Turn = Output[1]
      Output = []
      if Color == 1:
        # print("Paint White")
        if (CurrentRow, CurrentColumn) not in Painted:
          Painted.append((CurrentRow, CurrentColumn))
        if (CurrentRow, CurrentColumn) not in EverPainted:
          EverPainted.append((CurrentRow, CurrentColumn))
      if Color == 0:
        # print("Paint Black")
        if (CurrentRow, CurrentColumn) in Painted:
          Painted.remove((CurrentRow, CurrentColumn))
      if Turn == 1:
        # print("Turn Right")
        if Direction == "Up":
          Direction = "Right"
        elif Direction == "Right":
          Direction = "Down"
        elif Direction == "Down":
          Direction = "Left"
        elif Direction == "Left":
          Direction = "Up"
      if Turn == 0:
        # print("Turn Left")
        if Direction == "Right":
          Direction = "Up"
        elif Direction == "Down":
          Direction = "Right"
        elif Direction == "Left":
          Direction = "Down"
        elif Direction == "Up":
          Direction = "Left"
      if Direction == "Up":
        CurrentRow -= 1
      if Direction == "Right":
        CurrentColumn += 1
      if Direction == "Down":
        CurrentRow += 1
      if Direction == "Left":
        CurrentColumn -= 1
      # print(Painted)
    RealIndex += 2
    continue
    
  if Opcode == 5:
    First = GetVal(RealIndex + 1, Modes[0], RelativeBase)
    if First != 0:
      RealIndex = GetVal(RealIndex + 2, Modes[1], RelativeBase)
      continue
    RealIndex += 3
    continue
    
  if Opcode == 6:
    First = GetVal(RealIndex + 1, Modes[0], RelativeBase)
    if First == 0:
      RealIndex = GetVal(RealIndex + 2, Modes[1], RelativeBase)
      continue
    RealIndex += 3
    continue
    
  if Opcode == 7:
    First = GetVal(RealIndex + 1, Modes[0], RelativeBase)
    Second = GetVal(RealIndex + 2, Modes[1], RelativeBase)
    if First < Second:
      ValueIndexToUpdate = Values[Indexes.index(RealIndex + 3)]
      if Modes[2] == 2:
        Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = 1
      else:
        Values[Indexes.index(ValueIndexToUpdate)] = 1
    else:
      ValueIndexToUpdate = Values[Indexes.index(RealIndex + 3)]
      if Modes[2] == 2:
        Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = 0
      else:
        Values[Indexes.index(ValueIndexToUpdate)] = 0
    RealIndex += 4
    continue
    
  if Opcode == 8:
    First = GetVal(RealIndex + 1, Modes[0], RelativeBase)
    Second = GetVal(RealIndex + 2, Modes[1], RelativeBase)
    if First == Second:
      ValueIndexToUpdate = Values[Indexes.index(RealIndex + 3)]
      if ValueIndexToUpdate not in Indexes:
        Indexes.append(ValueIndexToUpdate)
        Values.append(0)
      if ValueIndexToUpdate + RelativeBase not in Indexes:
        Indexes.append(ValueIndexToUpdate + RelativeBase)
        Values.append(0)
      if Modes[2] == 2:
        Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = 1
      else:
        Values[Indexes.index(ValueIndexToUpdate)] = 1
    else:
      ValueIndexToUpdate = Values[Indexes.index(RealIndex + 3)]
      if ValueIndexToUpdate not in Indexes:
        Indexes.append(ValueIndexToUpdate)
        Values.append(0)
      if ValueIndexToUpdate + RelativeBase not in Indexes:
        Indexes.append(ValueIndexToUpdate + RelativeBase)
        Values.append(0)
      if Modes[2] == 2:
        Values[Indexes.index(ValueIndexToUpdate + RelativeBase)] = 0
      else:
        Values[Indexes.index(ValueIndexToUpdate)] = 0
    RealIndex += 4
    continue

  if Opcode == 9:
    Adjust = GetVal(RealIndex + 1, Modes[0], RelativeBase)
    RelativeBase += Adjust
    RealIndex += 2
    continue

MinRow = float('inf')
MinColumn = float('inf')
MaxRow = 0
MaxColumn = 0
for x in Painted:
  if x[0] < MinRow:
    MinRow = x[0]
  if x[1] < MinColumn:
    MinColumn = x[1]
  if x[0] > MaxRow:
    MaxRow = x[0]
  if x[1] > MaxColumn:
    MaxColumn = x[1]

print(Painted)

print(MinRow, MinColumn)
print(MaxRow, MaxColumn)

Grid = [[0 for y in range(MaxColumn + 1)] for x in range(MaxRow + 1)]

for x in Painted:
  Grid[x[0]][x[1]] = 1

for x in Grid:
  String = ""
  for y in x:
    if y:
      String = String + "█"
    else:
      String = String + " "
  print(String)
  