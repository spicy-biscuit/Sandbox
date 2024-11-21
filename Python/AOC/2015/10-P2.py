Input = "3113322113"

from functools import cache

@cache
def FirstThree(String):
  if len(String) == 0:
    return(["", 0])
  if len(String) == 1:
    return(["1" + String, 2])
  if String[1] == String[0]:
    if len(String) == 2:
      return(["2" + String[0], 2])
    if String[2] == String[1]:
      return(["3" + String[0], 3])
    else:
      return(["2" + String[0], 2])
  else:
    return(["1" + String[0], 1])

# @cache
def LookSay(String):
  Output = ""
  while String != "":
    Output = Output + FirstThree(String[:3])[0]
    String = String[FirstThree(String[:3])[1]:]
  return(Output)
  

for x in range(50):
  Input = LookSay(Input)
  print(x + 1, len(Input))

    