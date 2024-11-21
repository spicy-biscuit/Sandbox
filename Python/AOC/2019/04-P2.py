Input = "183564-657474"

Input = Input.split("-")
Input[0] = int(Input[0])
Input[1] = int(Input[1])

print(Input)

def CheckValid(Num):
  Num = str(Num)
  Num = "a" + Num + "a"
  This = False
  for x in range(1, 6):
    if Num[x] == Num[x + 1] and Num[x] != Num[x - 1] and Num[x] != Num[x + 2]:
      This = True
  if This == False:
    return(False)
  Num = Num[1:-1]
  for x in range(5):
    if int(Num[x]) > int(Num[x + 1]):
      return(False)
  return(True)


print(CheckValid(112233))
print(CheckValid(123444))
print(CheckValid(111122))
    
Total = 0
for Password in range(Input[0], Input[1] + 1):
  Total += CheckValid(Password)
print(Total)