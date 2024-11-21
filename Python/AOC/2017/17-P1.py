Input = 314
# Input = 3

Buffer = [0]
CurrentPosition = 0

def Step(BufferLength, CurrentPosition, StepAmount):
  CurrentPosition += StepAmount
  CurrentPosition %= BufferLength
  return(CurrentPosition)

for Cycle in range(1, 2017 + 1):
  CurrentPosition = Step(len(Buffer), CurrentPosition, Input)
  Buffer.insert(CurrentPosition + 1, Cycle)
  CurrentPosition += 1

print(Buffer)
print(Buffer[Buffer.index(2017) + 1])