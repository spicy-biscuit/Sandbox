'''
ID: ethanfung8
LANG: PYTHON3
PROG: gift1
'''

# File = open(r"USACO/Practice/Chapter 1/gift1/gift1.in", "r")
File = open(r"gift1.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")

Names = []
NumNames = int(Input[0])
Input = Input[1:]
Cash = []

for x in range(NumNames):
  Names.append(Input[0])
  Cash.append(0)
  Input = Input[1:]
# print(Names)

for x in range(NumNames):
  Giver = Input[0]
  Input = Input[1:]
  Numbers = Input[0]
  Input = Input[1:]
  Numbers = Numbers.split()
  NumMoney = int(Numbers[0])
  NumReceivers = int(Numbers[1])
  Receivers = []
  for x in range(NumReceivers):
    Receivers.append(Input[0])
    Input = Input[1:]
  # print(Giver, Receivers)
  
  if NumReceivers == 0:
    continue

  EachReceiverIncome = NumMoney // NumReceivers
  Cash[Names.index(Giver)] = Cash[Names.index(Giver)] - EachReceiverIncome * NumReceivers
  for Person in Receivers:
    Cash[Names.index(Person)] = Cash[Names.index(Person)] + EachReceiverIncome

# File = open(r"USACO/Practice/Chapter 1/gift1/gift1.out", "x")
File = open(r"gift.out", "x")

for x in range(NumNames):
  File.write(str(Names[x]) + " " + str(Cash[x]) + "\n")
File.close()