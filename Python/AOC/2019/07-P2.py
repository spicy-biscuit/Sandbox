def Intcode(InStats):
  #Input: For Opcodes of 3 & 4
  #Describes the input values of the program
  Input = InStats[1]
  #Output: For Opcodes of 3 & 4
  #Describes the output values of the program
  Output = InStats[2]
  
  #Instructions: The list of numbers that is both the 
  #memory and instruction of Intcode computers
  Instructions = InStats[3]
  #Index: The current Index of the program
  Index = InStats[4]
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
      return(["HALTED", Output])
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
      if Input == []:
        return(["CONTINUE", Input, Output, Instructions, Index])
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

RealInput = [3,8,1001,8,10,8,105,1,0,0,21,42,55,64,77,94,175,256,337,418,99999,3,9,102,4,9,9,1001,9,5,9,102,2,9,9,101,3,9,9,4,9,99,3,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,5,9,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99]
# RealInput = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]


def Function(Num):
  Out = []
  if Num == 0:
    return(["5"])
  if Num == 1:
    return(["56", "65"])
  List = Function(Num - 1)
  Out = []
  for x in List:
    for y in range(Num + 1):
      Out.append(x[:y] + str(Num + 5) + x[y:])
  return(Out)

def FunctionA(Num):
  Out = []
  if Num == 0:
    return(["0"])
  if Num == 1:
    return(["01", "10"])
  List = FunctionA(Num - 1)
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
  print(PhaseSetting)

  InA = []
  for x in RealInput:
    InA.append(x)
  
  InB = []
  for x in RealInput:
    InB.append(x)
  
  InC = []
  for x in RealInput:
    InC.append(x)
  
  InD = []
  for x in RealInput:
    InD.append(x)
  
  InE = []
  for x in RealInput:
    InE.append(x)

  InputA = [PhaseSetting[0], 0]
  InputB = [PhaseSetting[1]]
  InputC = [PhaseSetting[2]]
  InputD = [PhaseSetting[3]]
  InputE = [PhaseSetting[4]]
    
  AmpA = ["CONTINUE", InputA, InputB, InA, 0]
  AmpB = ["CONTINUE", InputB, InputC, InB, 0]
  AmpC = ["CONTINUE", InputC, InputD, InC, 0]
  AmpD = ["CONTINUE", InputD, InputE, InD, 0]
  AmpE = ["CONTINUE", InputE, InputA, InE, 0]

  while True:
    if AmpA[0] == "CONTINUE":
      AmpA = Intcode(AmpA)
      if AmpA[0] == "HALTED":
        AmpB[1] = AmpA[1]
      else:
        AmpB[1] = AmpA[2]
        AmpE[2] = AmpA[1]
      
    if AmpB[0] == "CONTINUE":
      AmpB = Intcode(AmpB)
      if AmpB[0] == "HALTED":
        AmpC[1] = AmpB[1]
      else:
        AmpC[1] = AmpB[2]
        AmpA[2] = AmpB[1]
      
    if AmpC[0] == "CONTINUE":
      AmpC = Intcode(AmpC)
      if AmpC[0] == "HALTED":
        AmpD[1] = AmpC[1]
      else:
        AmpD[1] = AmpC[2]
        AmpB[2] = AmpC[1]
      
    if AmpD[0] == "CONTINUE":
      AmpD = Intcode(AmpD)
      if AmpD[0] == "HALTED":
        AmpE[1] = AmpD[1]
      else:
        AmpE[1] = AmpD[2]
        AmpC[2] = AmpD[1]
      
    if AmpE[0] == "CONTINUE":
      AmpE = Intcode(AmpE)
      if AmpE[0] == "HALTED":
        AmpA[1] = AmpE[1]
      else:
        AmpA[1] = AmpE[2]
        AmpD[2] = AmpE[1]

    if AmpA[0] == "HALTED" and AmpB[0] == "HALTED" and AmpC[0] == "HALTED" and AmpD[0] == "HALTED" and AmpE[0] == "HALTED":
      print(AmpA)
      print(AmpB)
      print(AmpC)
      print(AmpD)
      print(AmpE)
      Out = (AmpE[1][-1])
      if Out > Max:
        Max = Out
      break

print()
print(Max)