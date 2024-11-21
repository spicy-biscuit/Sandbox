Input = "uqwqemis"

# Input = "abc"

import hashlib

Password = "________"
Open = [True for x in range(8)]
AppendThis = -1
while True:
  AppendThis += 1
  String = Input + str(AppendThis)
  String = hashlib.md5(String.encode())
  String = String.hexdigest()
  if String[:5] == "00000":
    # print("hi")
    if String[5] in ["0", "1", "2", "3", "4", "5", "6", "7"]:
      if Open[int(String[5])]:
        Password = Password[:int(String[5])] + String[6] + Password[int(String[5]) + 1:]
        Open[int(String[5])] = False
        print(Password)
        if Open == [False for x in range(8)]:
          break
      