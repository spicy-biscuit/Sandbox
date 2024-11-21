Input = "183564-657474"

Input = Input.split("-")
Input[0] = int(Input[0])
Input[1] = int(Input[1])

print(Input)

def CheckValid(Num):
  Num = str(Num)
  This = False
  for x in range(5):
    if Num[x] == Num[x + 1]:
      This = True
  if This == False:
    return(False)
  for x in range(5):
    if int(Num[x]) > int(Num[x + 1]):
      return(False)
  return(True)


print(CheckValid(111111))
print(CheckValid(223450))
print(CheckValid(123789))
    
Total = 0
for Password in range(Input[0], Input[1] + 1):
  Total += CheckValid(Password)
print(Total)