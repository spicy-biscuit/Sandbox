'''
ID: ethanfung8
LANG: PYTHON3
PROG: ride
'''

# File = open(r"USACO/Practice/Chapter 1/Ride/ride.in", "r")
File = open(r"ride.in", "r")
Input = File.read()
File.close()

Input = Input.split("\n")
CometName = Input[0]
GroupName = Input[1]
CometNumber = 1
GroupNumber = 1

for x in range(len(CometName)):
  CometNumber = CometNumber * (ord(CometName[x]) - 64)
CometNumber = CometNumber % 47

for x in range(len(GroupName)):
  GroupNumber = GroupNumber * (ord(GroupName[x]) - 64)
GroupNumber = GroupNumber % 47

# File = open(r"USACO/Practice/Chapter 1/Ride/ride.out", "x")
File = open(r"ride.out", "x")

if CometNumber == GroupNumber:
  File.write("GO\n")
else:
  File.write("STAY\n")
File.close()