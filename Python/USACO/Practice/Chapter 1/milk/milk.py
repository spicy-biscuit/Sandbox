'''
ID: ethanfung8
LANG: PYTHON3
PROG: milk
'''

# File = open(r"USACO/Practice/Chapter 1/milk/milk.in", "r")
File = open(r"milk.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")
Nums = Input[0].split()
Farmers = Input[1:]

N = int(Nums[0])
M = int(Nums[1])

if Farmers[-1] == "":
  Farmers = Farmers[:-1]
for x in range(len(Farmers)):
  Farmers[x] = Farmers[x].split()
  print(Farmers[x])
  Farmers[x] = (int(Farmers[x][0]), int(Farmers[x][1]))

# print(Farmers)

Out = 0
while True:
  MinCost = float('inf')
  Supply = 0
  ThisFarmer = ()
  for Farmer in Farmers:
    Cost = Farmer[0]
    if Cost < MinCost:
      MinCost = Cost
      Supply = Farmer[1]
      ThisFarmer = Farmer
  print(MinCost, min(Supply, N))
  if Supply == 0:
    break
  if Supply >= N:
    Out += N * MinCost
    break
  else:
    N -= Supply
    Out += Supply * MinCost
    Farmers.remove(ThisFarmer)

print(Out)
# File = open(r"USACO/Practice/Chapter 1/milk/milk.out", "x")
File = open(r"milk.out", "x")
File.write(str(Out) + "\n")
File.close()