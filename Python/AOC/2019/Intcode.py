Input = []
Output = []
Instructions = []
Values = []
Indexes = []

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
    
print(Output)