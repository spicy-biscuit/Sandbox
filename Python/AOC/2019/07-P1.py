def Intcode(InInstructions, InSignal, InPhase):
  #Input: For Opcodes of 3 & 4
  #Describes the input values of the program
  Input = [InPhase, InSignal]
  #Output: For Opcodes of 3 & 4
  #Describes the output values of the program
  Output = []
  
  #Instructions: The list of numbers that is both the 
  #memory and instruction of Intcode computers
  Instructions = []
  for x in InInstructions:
    Instructions.append(x)
  #Index: The current Index of the program
  Index = 0
  #Modes: What mode the program is in.
  #0: Position mode. 50 means the number at address 50.
  #1: Immediate mode. 50 means 50.
  def GetVal(Value, Mode):
    if Mode == 1:
      return(Value)
    if Mode == 0:
      return(Instructions[Value])
  
  while True:
    Opcode = Instructions[Index] % 100
    
    if Opcode == 99:
      break
  
    Modes = []
    # print(Instructions[Index])
    Modes.append(int((Instructions[Index] % 1000 - Instructions[Index] % 100) / 100))
    Modes.append(int((Instructions[Index] % 10000 - Instructions[Index] % 1000) / 1000))
    Modes.append(int((Instructions[Index] % 100000 - Instructions[Index] % 10000) / 10000))
    # print(Modes)
    
    if Opcode == 1:
      Instructions[Instructions[Index + 3]] = GetVal(Instructions[Index + 1], Modes[0]) + GetVal(Instructions[Index + 2], Modes[1])
      Index += 4
      continue
      
    if Opcode == 2:
      Instructions[Instructions[Index + 3]] = GetVal(Instructions[Index + 1], Modes[0]) * GetVal(Instructions[Index + 2], Modes[1])
      Index += 4
      continue
      
    if Opcode == 3:
      Instructions[Instructions[Index + 1]] = Input[0]
      Input = Input[1:]
      Index += 2
      continue
      
    if Opcode == 4:
      Output.append(GetVal(Instructions[Index + 1], Modes[0]))
      Index += 2
      continue
      
    if Opcode == 5:
      First = GetVal(Instructions[Index + 1], Modes[0])
      if First != 0:
        Index = GetVal(Instructions[Index + 2], Modes[1])
        continue
      Index += 3
      continue
      
    if Opcode == 6:
      First = GetVal(Instructions[Index + 1], Modes[0])
      if First == 0:
        Index = GetVal(Instructions[Index + 2], Modes[1])
        continue
      Index += 3
      continue
      
    if Opcode == 7:
      First = GetVal(Instructions[Index + 1], Modes[0])
      Second = GetVal(Instructions[Index + 2], Modes[1])
      if First < Second:
        Instructions[Instructions[Index + 3]] = 1
      else:
        Instructions[Instructions[Index + 3]] = 0
      Index += 4
      continue
      
    if Opcode == 8:
      First = GetVal(Instructions[Index + 1], Modes[0])
      Second = GetVal(Instructions[Index + 2], Modes[1])
      if First == Second:
        Instructions[Instructions[Index + 3]] = 1
      else:
        Instructions[Instructions[Index + 3]] = 0
      Index += 4
      continue
  return(Output)

RealInput = [3,8,1001,8,10,8,105,1,0,0,21,42,55,64,77,94,175,256,337,418,99999,3,9,102,4,9,9,1001,9,5,9,102,2,9,9,101,3,9,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,5,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99]
# RealInput = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# RealInput = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# RealInput = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def Function(Num):
  Out = []
  if Num == 0:
    return(["0"])
  if Num == 1:
    return(["01", "10"])
  List = Function(Num - 1)
  Out = []
  for x in List:
    for y in range(Num + 1):
      Out.append(x[:y] + str(Num) + x[y:])
  return(Out)

Max = 0
for PhaseSetting in Function(4):
  PhaseSetting = list(PhaseSetting)
  for x in range(5):
    PhaseSetting[x] = int(PhaseSetting[x])
  SignalIn = 0
  for x in range(5):
    SignalIn = Intcode(RealInput, SignalIn, PhaseSetting[x])[0]
  if SignalIn > Max:
    Max = SignalIn
print(Max)