Input = 314
# Input = 3

# Buffer = [0]
CurrentPosition = 0

def Step(BufferLength, CurrentPosition, StepAmount):
  CurrentPosition += StepAmount
  CurrentPosition %= BufferLength
  return(CurrentPosition)

Output = 1
for Cycle in range(1, 50000000 + 1):
  CurrentPosition = Step(Cycle, CurrentPosition, Input)
  if CurrentPosition == 0:
    Output = Cycle
  CurrentPosition += 1
  
print(Output)