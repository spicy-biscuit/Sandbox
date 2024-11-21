Input = "bgvyzdsv"
# Input = "pqrstuv"

import hashlib

from functools import cache

AppendThis = -1

@cache
def FindZeroes(String):
  if String[0] == "0":
    return(1 + FindZeroes(String[1:]))
  return(0)

MaxZeroes = 0
while True:
  AppendThis += 1
  String = Input + str(AppendThis)
  String = hashlib.md5(String.encode())
  String = String.hexdigest()
  Zeroes = FindZeroes(String)
  if Zeroes >= MaxZeroes:
    MaxZeroes = Zeroes
    print(String)
  if Zeroes == 6:
    print(AppendThis)
    break