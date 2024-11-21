Input = [463, 71787]

# Input = [30, 5807]
# Input = [21, 6111]
# Input = [17, 1104]
# Input = [13, 7999]
# Input = [10, 1618]
# Input = [9, 25]

Input[1] *= 100

from functools import cache
import numpy
from collections import deque 

Marbles = deque([4, 2, 1, 3, 0])
# Marbles = numpy.array([4, 2, 1, 3, 0])
CurrentMarble = 4
CurrentPlayer = 4
Scores = [0 for x in range(Input[0] + 10)]

@cache
def Back(Player, Players):
  if Player >= Players:
    Player -= Players
  return(Player)

while True:
  CurrentMarble += 1
  CurrentPlayer += 1
  # if CurrentMarble % (Input[1] / 100) == 0:
  #   print(100 * CurrentMarble / Input[1])
  CurrentPlayer = Back(CurrentPlayer, Input[0])

  if CurrentMarble % 23 == 0:
    # Marbles.printLL()
    Marbles.rotate(7)
    Scores[CurrentPlayer] += CurrentMarble + Marbles.popleft()
    # Marbles = numpy.concatenate((Marbles[-6:], Marbles[:-7]))
    # for x in range(7):
    #   Marbles.insertAtBegin(Marbles.valueAtIndex(Marbles.sizeOfLL() - 1))
    #   Marbles.remove_last_node()
    # Marbles.remove_first_node()
    # print('HIHI')
    # break
  else:
    # Marbles.insertAtEnd(Marbles.valueAtIndex(0))
    # Marbles.remove_first_node()
    # Marbles.insertAtEnd(Marbles.valueAtIndex(0))
    # Marbles.remove_first_node()
    # Marbles.insertAtBegin(CurrentMarble)
    Marbles.rotate(-2)
    Marbles.appendleft(CurrentMarble)
    # Marbles = numpy.concatenate((numpy.array([CurrentMarble]), Marbles[2:], Marbles[:2]))
    # Marbles = [CurrentMarble] + Marbles[2:] + Marbles[:2]

  if CurrentMarble >= Input[1]:
    break

# Marbles.printLL()
# print(Marbles)
print(max(Scores))