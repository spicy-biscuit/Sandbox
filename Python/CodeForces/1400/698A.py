"""
698A: Vacations
"""

N = int(input())

A = tuple(map(int, input().split()))
from functools import cache
# print(A)
@cache
def Function(DidSport, DidWrite, Remaining):
  # print(len(Remaining))
  # if len(Remaining) > 80:
  #   print(len(Remaining))
  if len(Remaining) == 0:
    return(0)
  ThisDay = Remaining[0]
  Remaining = Remaining[1:]
  CanSport = False
  CanWrite = False
  if ThisDay in [1, 3]:
    CanWrite = True
  if ThisDay in [2, 3]:
    CanSport = True

  if DidSport:
    CanSport = False
  if DidWrite:
    CanWrite = False

  List = []

  if CanSport:
    List.append(Function(True, False, Remaining))
  if CanWrite:
    List.append(Function(False, True, Remaining))
  List.append(1 + Function(False, False, Remaining))
  return(min(List))


print(Function(False, False, A))

"""
ACCEPTED!
"""