input = """jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""

Instructions = input.split("\n")

RegA = 1
RegB = 0
CurrentInstruction = 0

while True:
    InstructionType = Instructions[CurrentInstruction][:3]
    if InstructionType == "hlf":
        Register = Instructions[CurrentInstruction][4]
        if Register == "a":
            RegA = RegA / 2
        else:
            RegB = RegB / 2
        CurrentInstruction += 1
    elif InstructionType == "tpl":
        Register = Instructions[CurrentInstruction][4]
        if Register == "a":
            RegA = RegA * 3
        else:
            RegB = RegB * 3
        CurrentInstruction += 1
    elif InstructionType == "inc":
        Register = Instructions[CurrentInstruction][4]
        if Register == "a":
            RegA = RegA + 1
        else:
            RegB = RegB + 1
        CurrentInstruction += 1
    elif InstructionType == "jmp":
        Offset = Instructions[CurrentInstruction][4:]
        Offset = int(Offset)
        CurrentInstruction += Offset
    elif InstructionType == "jie":
        Register = Instructions[CurrentInstruction][4]
        Offset = Instructions[CurrentInstruction][7:]
        Offset = int(Offset)
        if Register == "a":
            if RegA % 2 == 0:
                CurrentInstruction += Offset
            else:
                CurrentInstruction += 1
        if Register == "b":
            if RegB % 2 == 0:
                CurrentInstruction += Offset
            else:
                CurrentInstruction += 1
    elif InstructionType == "jio":
        Register = Instructions[CurrentInstruction][4]
        Offset = Instructions[CurrentInstruction][7:]
        Offset = int(Offset)
        if Register == "a":
            if RegA == 1:
                CurrentInstruction += Offset
            else:
                CurrentInstruction += 1
        if Register == "b":
            if RegB == 1:
                CurrentInstruction += Offset
            else:
                CurrentInstruction += 1
    if CurrentInstruction >= len(Instructions):
        break
    print(Instructions[CurrentInstruction], RegB)
print(RegB)
        