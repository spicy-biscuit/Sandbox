Input = "vzbxkghb"

def PasswordToList(Password):
  List = []
  for x in range(len(Password)):
    x = Password[x]
    List.append(ord(x) - 96)
  return(List)

def ListToPassword(List):
  Password = ""
  for x in List:
    Password = Password + chr(x + 96)
  return(Password)

def RequirementOne(Password):
  for x in range(len(Password) - 2):
    if Password[x] + 2 == Password[x + 1] + 1 and Password[x] + 2 == Password[x + 2]:
      return(True)
  return(False)

def RequirementTwo(Password):
  for x in Password:
    if x in [9, 12, 15]:
      return(False)
  return(True)

def RequirementThree(Password):
  PairIndexes = []
  for x in range(len(Password) - 1):
    if Password[x] == Password[x + 1]:
      PairIndexes.append(x)
  for x in PairIndexes:
    for y in PairIndexes:
      if y not in [x - 1, x, x + 1]:
        return(True)
  return(False)

def AllReqs(Password):
  return(RequirementOne(Password) and RequirementTwo(Password) and RequirementThree(Password))

def IncrementPassword(Password):
  Password[7] = Password[7] + 1
  if Password[7] == 27:
    Password[7] = 1
    Password[6] = Password[6] + 1
  if Password[6] == 27:
    Password[6] = 1
    Password[5] = Password[5] + 1
  if Password[5] == 27:
    Password[5] = 1
    Password[4] = Password[4] + 1
  if Password[4] == 27:
    Password[4] = 1
    Password[3] = Password[3] + 1
  if Password[3] == 27:
    Password[3] = 1
    Password[2] = Password[2] + 1
  if Password[2] == 27:
    Password[2] = 1
    Password[1] = Password[1] + 1
  if Password[1] == 27:
    Password[1] = 1
    Password[0] = Password[0] + 1
  return(Password)

CurrentPassword = PasswordToList(Input)

while True:
  CurrentPassword = IncrementPassword(CurrentPassword)
  if AllReqs(CurrentPassword):
    print(ListToPassword(CurrentPassword))
    break

while True:
  CurrentPassword = IncrementPassword(CurrentPassword)
  if AllReqs(CurrentPassword):
    print(ListToPassword(CurrentPassword))
    break
  