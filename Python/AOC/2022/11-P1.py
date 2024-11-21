Input = ["""Monkey 0:
  Starting items: 66, 79
  Operation: new = old * 11
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 7

Monkey 1:
  Starting items: 84, 94, 94, 81, 98, 75
  Operation: new = old * 17
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 2:
  Starting items: 85, 79, 59, 64, 79, 95, 67
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 4
    If false: throw to monkey 5

Monkey 3:
  Starting items: 70
  Operation: new = old + 3
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 4:
  Starting items: 57, 69, 78, 78
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 65, 92, 60, 74, 72
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 3
    If false: throw to monkey 4

Monkey 6:
  Starting items: 77, 91, 91
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 7:
  Starting items: 76, 58, 57, 55, 67, 77, 54, 99
  Operation: new = old + 6
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 1"""]

# Input = ["""Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""]

Input = Input[0].split("\n\n")

MonkeyData = []
HeldItems = []
Monkeys = len(Input)

for Monkey in Input:
  List = []
  Monkey = Monkey.split("\n")
  Monkey = Monkey[1:]
  
  Items = Monkey[0]
  Operation = Monkey[1]
  Test = Monkey[2]
  IfTrue = Monkey[3]
  IfFalse = Monkey[4]

  Items = Items[Items.find(":") + 1:][1:]
  Items = Items.split(", ")
  for x in range(len(Items)):
    Items[x] = int(Items[x])

  Operation = Operation[Operation.find("old") + 4:]
  ActualOperation = Operation[0]
  Operation = Operation[2:]
  Operation = [ActualOperation, Operation]

  Test = int(Test[Test.find("by") + 3:])

  IfTrue = int(IfTrue[IfTrue.find("monkey") + 7:])
  
  IfFalse = int(IfFalse[IfFalse.find("monkey") + 7:])

  HeldItems.append(Items)
  MonkeyData.append([Operation, Test, IfTrue, IfFalse])

def Throw(Item, Monkey):
  # print("-----")
  # print(Item)
  Operation = MonkeyData[Monkey][0]
  Test = MonkeyData[Monkey][1]
  IfTrue = MonkeyData[Monkey][2]
  IfFalse = MonkeyData[Monkey][3]
  
  ActualOperation = Operation[0]
  Value = Operation[1]
  if Value.isdigit():
    Value = int(Operation[1])
  if Value == "old":
    Value = Item
  if ActualOperation == "*":
    Item *= Value
  if ActualOperation == "+":
    Item += Value

  Item = Item // 3

  # print(Item)
  if Item % Test == 0:
    HeldItems[IfTrue].append(Item)
  else:
    HeldItems[IfFalse].append(Item)

for x in range(len(HeldItems)):
  for y in range(len(HeldItems[x])):
    HeldItems[x][y] = int(HeldItems[x][y])

Indexes = [0 for x in range(Monkeys)]

for ROUND in range(20):
  
  for Monkey in range(Monkeys):
    Indexes[Monkey] += len(HeldItems[Monkey])
    for Item in HeldItems[Monkey]:
      Throw(Item, Monkey)
    HeldItems[Monkey] = []


print(Indexes)
Out = 1
Out *= max(Indexes)
Indexes.remove(max(Indexes))
Out *= max(Indexes)
print(Out)