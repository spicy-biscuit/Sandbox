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

# Input = ["""set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2"""]

Input = Input[0].split("\n")

Index = 0

Sounds = []
Registers = []
Values = []

def Value(Item):
  if Item.isdigit():
    return(int(Item))
  if Item[0] == "-":
    return(-1 * int(Item[1:]))
  Index = Registers.index(Item)
  return(Values[Index])
  
for Instruction in Input:
  Instruction = Instruction.split()
  if not Instruction[1].isdigit() and Instruction[1][0] != "-":
    if Instruction[1] not in Registers:
      Registers.append(Instruction[1])
      Values.append(0)
  if len(Instruction) == 2:
    continue
  if not Instruction[2].isdigit() and Instruction[2][0] != "-":
    if Instruction[2] not in Registers:
      Registers.append(Instruction[2])
      Values.append(0)
print(Registers)

while True:
  if Index < 0 or Index >= len(Input):
    break
  Instruction = Input[Index]
  print(Instruction)
  Instruction = Instruction.split()
  if Instruction[0] == "snd":
    Sounds.append(Value(Instruction[1]))
    Index += 1
    continue
  if Instruction[0] == "set":
    Values[Registers.index(Instruction[1])] = Value(Instruction[2])
    Index += 1
    continue
  if Instruction[0] == "add":
    Values[Registers.index(Instruction[1])] += Value(Instruction[2])
    Index += 1
    continue
  if Instruction[0] == "mul":
    Values[Registers.index(Instruction[1])] *= Value(Instruction[2])
    Index += 1
    continue
  if Instruction[0] == "mod":
    Values[Registers.index(Instruction[1])] %= Value(Instruction[2])
    Index += 1
    continue
  if Instruction[0] == "rcv":
    if Value(Instruction[1]) != 0:
      Values[Registers.index(Instruction[1])] = Sounds[0]
      break
    Index += 1
    continue
  if Instruction[0] == "jgz":
    if Value(Instruction[1]) > 0:
      Index += Value(Instruction[2])
      continue
    Index += 1
    continue


print(Sounds[-1])
    