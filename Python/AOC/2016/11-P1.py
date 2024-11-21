Input = ["""The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant."""]

Input = [[["promethium", "generator"], ["promethium", "chip"]], [["cobalt", "generator"], ["curium", "generator"], ["ruthenium", "generator"], ["plutonium", "generator"]], [["cobalt", "chip"], ["curium", "chip"], ["ruthenium", "chip"], ["plutonium", "chip"]], []]

#Sample
Input = [[["hydrogen", "chip"], ["lithium", "chip"]], [["hydrogen", "generator"]], [["lithium", "generator"]], []]

"""
Format:

[[Floor1 items], [Floor2 items], [Floor 3 items], [Floor 4 items]]

Function:
takes every possible combination of items on current floor
tries incrementing/decrementing floor
if floor layout is invalid, breakout
if steps > minsteps, breakout
if floor1, 2, and 3 are empty: return steps
"""

"""
Rule:
if a chip is in a room with a generator:
  it must have it's own generator in the room.
"""

def ValidFloor(Floor):
  for ITEM in Floor:
    if ITEM[1] == "generator":
      break
    else:
      return(True)
  for ITEM in Floor:
    if ITEM[1] == "chip":
      Type = ITEM[0]
      Valid = False
      for SearchItem in Floor:
        if SearchItem == [Type, "generator"]:
          Valid = True
          break
      if not Valid:
        return(False)
  return(True)
  
def ValidSetup(Floors):
  for Floor in Floors:
    if ValidFloor(Floor) == False:
      return(False)
  return(True)

