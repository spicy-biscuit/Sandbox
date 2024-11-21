Input = [12,1,16,3,11,0]

# Input = [0, 3, 6]
# Input = [1,3,2]

AllNums = []

Last = 0
First = True
for x in range(2020 + 5):
  if Input != []:
    Now = Input[0]
    Input = Input[1:]
  else:
    # if First:
    #   AllNums = AllNums[1:]
    #   First = False
    if Last in AllNums:
      Index = 0
      for y in range(len(AllNums)):
        if AllNums[y] == Last:
          Index = y
      Now = x - Index - 1
    else:
      Now = 0
  # print(Now)
  if not First:
    AllNums.append(Last)
  First = False
  Last = Now

# print(AllNums)

print(AllNums[2019])
    
  