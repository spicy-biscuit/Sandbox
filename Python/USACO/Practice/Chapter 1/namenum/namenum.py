'''
ID: ethanfung8
LANG: PYTHON3
PROG: namenum
'''

# File = open(r"USACO/Practice/Chapter 1/namenum/namenum.in", "r")
File = open(r"namenum.in", "r")
Input = File.read()
File.close()

# File = open(r"USACO/Practice/Chapter 1/namenum/dict.txt", "r")
File = open(r"dict.txt", "r")
Dictionary = File.read()
File.close()

Dictionary = Dictionary.split("\n")

Letters = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "R", "S"], ["T", "U", "V"], ["W", "X", "Y"]]

List = []
Input = Input[:-1]
# print(Input)
for Name in Dictionary:
  # print("-----")
  IsName = True
  if len(Name) != len(Input):
    continue
  for x in range(len(Input)):
    y = x
    x = Input[x]
    if x == "0" or x == "1":
      IsName = False
      break
    ThisLetters = Letters[int(x) - 2]
    # print(ThisLetters)
    if Name[y] not in ThisLetters:
      IsName = False
  if IsName:
    List.append(Name)

print(List)
if len(List) == 0:
  List = ["NONE"]


# File = open(r"USACO/Practice/Chapter 1/namenum/namenum.out", "x")
File = open(r"namenum.out", "x")
for x in List:
  File.write(x + "\n")
File.close()