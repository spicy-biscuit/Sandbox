Input = "bgvyzdsv"

import hashlib

AppendThis = -1
while True:
  AppendThis += 1
  String = Input + str(AppendThis)
  String = hashlib.md5(String.encode())
  String = String.hexdigest()
  if String[:3] == "000":
    print(String)
  if String[:5] == "00000":
    print(AppendThis)
    break