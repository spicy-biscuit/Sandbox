Input = ["""set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 622
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""]

# Input = ["""snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d"""]

Input = Input[0].split("\n")

Index1 = 0
Index0 = 0

Registers1 = []
Values1 = []
Registers0 = []
Values0 = []
Queue1 = []
Queue0 = []
Output = 0

def Value(Item, Register):
  if Item.isdigit():
    return(int(Item))
  if Item[0] == "-":
    return(-1 * int(Item[1:]))
  if Register == 1:
    Index = Registers1.index(Item)
    return(Values1[Index])
  if Register == 0:
    Index = Registers0.index(Item)
    return(Values0[Index])
  
for Instruction in Input:
  Instruction = Instruction.split()
  if not Instruction[1].isdigit() and Instruction[1][0] != "-":
    if Instruction[1] not in Registers1:
      Registers1.append(Instruction[1])
      Values1.append(0)
      Registers0.append(Instruction[1])
      Values0.append(0)
  if len(Instruction) == 2:
    continue
  if not Instruction[2].isdigit() and Instruction[2][0] != "-":
    if Instruction[2] not in Registers1:
      Registers1.append(Instruction[1])
      Values1.append(0)
      Registers0.append(Instruction[1])
      Values0.append(0)

Values1[Registers1.index("p")] = 1

while True:
  Break0 = False
  Break1 = False

  #Process Register0
  Instruction = Input[Index0]
  # print(Values0)
  # print(Instruction)
  Instruction = Instruction.split()
  if Instruction[0] == "snd":
    Queue1.append(Value(Instruction[1], 0))
    Index0 += 1
  elif Instruction[0] == "set":
    Values0[Registers0.index(Instruction[1])] = Value(Instruction[2], 0)
    Index0 += 1
  elif Instruction[0] == "add":
    Values0[Registers0.index(Instruction[1])] += Value(Instruction[2], 0)
    Index0 += 1
  elif Instruction[0] == "mul":
    Values0[Registers0.index(Instruction[1])] *= Value(Instruction[2], 0)
    Index0 += 1
  elif Instruction[0] == "mod":
    Values0[Registers0.index(Instruction[1])] %= Value(Instruction[2], 0)
    Index0 += 1
  elif Instruction[0] == "rcv":
    if len(Queue0) != 0:
      Values0[Registers0.index(Instruction[1])] = Queue0[0]
      Queue0 = Queue0[1:]
    else:
      Break0 = True
      Index0 -= 1
    Index0 += 1
  if Instruction[0] == "jgz":
    if Value(Instruction[1], 0) > 0:
      Index0 += Value(Instruction[2], 0)
    else:
      Index0 += 1

  #Process Register1
  Instruction = Input[Index1]
  # print(Values0)
  # print(Instruction)
  Instruction = Instruction.split()
  if Instruction[0] == "snd":
    Queue0.append(Value(Instruction[1], 1))
    Output += 1
    Index1 += 1
  elif Instruction[0] == "set":
    Values1[Registers1.index(Instruction[1])] = Value(Instruction[2], 1)
    Index1 += 1
  elif Instruction[0] == "add":
    Values1[Registers1.index(Instruction[1])] += Value(Instruction[2], 1)
    Index1 += 1
  elif Instruction[0] == "mul":
    Values1[Registers1.index(Instruction[1])] *= Value(Instruction[2], 1)
    Index1 += 1
  elif Instruction[0] == "mod":
    Values1[Registers1.index(Instruction[1])] %= Value(Instruction[2], 1)
    Index1 += 1
  elif Instruction[0] == "rcv":
    if len(Queue1) != 0:
      Values1[Registers1.index(Instruction[1])] = Queue1[0]
      Queue1 = Queue1[1:]
    else:
      Break1 = True
      Index1 -= 1
    Index1 += 1
  if Instruction[0] == "jgz":
    if Value(Instruction[1], 1) > 0:
      Index1 += Value(Instruction[2], 1)
    else:
      Index1 += 1

  print(Output, Values0, Values1)
  if Break0 and Break1:
    break

print(Output)

  
  
  