Input = ["""set b 79
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""]

Input = Input[0].split("\n")

Index = 0

Registers = [chr(x + 97) for x in range(8)]
Values = [0 for x in range(8)]

def Value(Item):
  if Item.isdigit():
    return(int(Item))
  if Item[0] == "-":
    return(-1 * int(Item[1:]))
  Index = Registers.index(Item)
  return(Values[Index])

print(Registers)

Output = 0
while True:
  if Index < 0 or Index >= len(Input):
    break
  Instruction = Input[Index]
  # print(Instruction)
  Instruction = Instruction.split()
  
  if Instruction[0] == "set":
    Values[Registers.index(Instruction[1])] = Value(Instruction[2])
    Index += 1
    continue
  if Instruction[0] == "sub":
    Values[Registers.index(Instruction[1])] -= Value(Instruction[2])
    Index += 1
    continue
  if Instruction[0] == "mul":
    Values[Registers.index(Instruction[1])] *= Value(Instruction[2])
    Index += 1
    Output += 1
    continue
  if Instruction[0] == "jnz":
    if Value(Instruction[1]) != 0:
      Index += Value(Instruction[2])
      continue
    Index += 1
    continue

print(Output)