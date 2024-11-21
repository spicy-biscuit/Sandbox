Input = 520185742

#Debugging
# Input = 1

Total = 0
for NUMBER in range(Input+1):
  if NUMBER % 100000 == 0:
    print(round(NUMBER/Input, 5))
  NUMBER = str(NUMBER)
  Flag = True
  for x in range(len(NUMBER)-1):
    if int(NUMBER[x+1]) < int(NUMBER[x]):
      Flag = False
      break
  if Flag:
    Total += 1

print(Total)