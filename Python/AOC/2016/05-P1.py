Input = "uqwqemis"

# Input = "abc"

import hashlib

Password = ""
AppendThis = -1
while True:
  AppendThis += 1
  String = Input + str(AppendThis)
  String = hashlib.md5(String.encode())
  String = String.hexdigest()
  if String[:5] == "00000":
    Password = Password + String[5]
    print(Password)
    if len(Password) == 8:
      break
      