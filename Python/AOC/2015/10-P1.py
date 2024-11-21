Input = "3113322113"

from functools import cache

# @cache
def LookSay(String):
  Output = ""
  while String != "":
    if len(String) == 1:
      return(Output + "1" + String)
    if String[1] == String[0]:
      if len(String) == 2:
        return(Output + "2" + String[0])
      if String[2] == String[1]:
        Output = Output + "3" + String[0]
        String = String[3:]
      else:
        Output = Output + "2" + String[0]
        String = String[2:]
    else:
      Output = Output + "1" + String[0]
      String = String[1:]
  return(Output)
  
# Input = "1"
for x in range(40):
  Input = LookSay(Input)
  print(x + 1, len(Input))

    