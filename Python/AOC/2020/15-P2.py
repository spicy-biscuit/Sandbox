Input = [12,1,16,3,11,0]

# Input = [0, 3, 6]
# Input = [1,3,2]

AllNums = {}

Seen = set([])

Last = -1
for x in range(30000000):
  if x % 100000 == 0:
    print(x)
  if Input != []:
    Now = Input[0]
    Input = Input[1:]
  else:
    if Last in Seen:
      Now = x - AllNums[Last]
      # print(Now)
    else:
      Now = 0
  AllNums[Last] = x
  Seen.add(Last)
  # print(Seen)
  # print(AllNums)
  Last = Now
  # print(Last)

print(Last)