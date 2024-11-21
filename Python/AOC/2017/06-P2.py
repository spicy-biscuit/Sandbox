Input = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"

# Input = "0 2 7 0"

Input = Input.split()

for x in range(len(Input)):
  Input[x] = int(Input[x])

print(Input)

PreviousStates = []

def Update(Banks):
  MaxBlocks = max(Banks)
  Index = Banks.index(MaxBlocks)
  Banks[Index] = 0
  for x in range(MaxBlocks):
    Index += 1
    if Index >= len(Banks):
      Index -= len(Banks)
    Banks[Index] = Banks[Index] + 1
  # return(Banks)

Steps = 0
while True:
  if Input in PreviousStates:
    print(Steps - PreviousStates.index(Input))
    break
  AppendThis = []
  for x in Input:
    AppendThis.append(x)
  PreviousStates.append(AppendThis)
  Steps += 1
  Update(Input)
  # print(Input)
    
  