State = 'A'

Marked = set([])
Position = 0

for STEPS in range(12368930):
  if Position in Marked:
    Slot = 1
  else:
    Slot = 0

  if State == "A":
    if Slot == 0:
      Marked.add(Position)
      Position += 1
      State = "B"
    if Slot == 1:
      Marked.remove(Position)
      Position += 1
      State = "C"
      
  elif State == "B":
    if Slot == 0:
      Position -= 1
      State = "A"
    if Slot == 1:
      Marked.remove(Position)
      Position += 1
      State = "D"
      
  elif State == "C":
    if Slot == 0:
      Marked.add(Position)
      Position += 1
      State = "D"
    if Slot == 1:
      Position += 1
      State = "A"
      
  elif State == "D":
    if Slot == 0:
      Marked.add(Position)
      Position -= 1
      State = "E"
    if Slot == 1:
      Marked.remove(Position)
      Position -= 1
      State = "D"
      
  elif State == "E":
    if Slot == 0:
      Marked.add(Position)
      Position += 1
      State = "F"
    if Slot == 1:
      Position -= 1
      State = "B"
      
  elif State == "F":
    if Slot == 0:
      Marked.add(Position)
      Position += 1
      State = "A"
    if Slot == 1:
      Position += 1
      State = "E"

print(len(Marked))

