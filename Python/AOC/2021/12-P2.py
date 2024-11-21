Input = ["""by-TW
start-TW
fw-end
QZ-end
JH-by
ka-start
ka-by
end-JH
QZ-cv
vg-TI
by-fw
QZ-by
JH-ka
JH-vg
vg-fw
TW-cv
QZ-vg
ka-TW
ka-QZ
JH-fw
vg-hu
cv-start
by-cv
ka-cv"""]

# Input = ["""fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""]

Input = Input[0].split("\n")

First = []
Second = []

for x in Input:
  x = x.split("-")
  First.append(x[0])
  First.append(x[1])
  Second.append(x[1])
  Second.append(x[0])

print(First)
print(Second)

def Function(Visited, Twice):
  CurrentCave = Visited[-1]
  if CurrentCave == "end":
    # print(Visited)
    return(1)
  if CurrentCave == "start" and Visited != ["start"]:
    return(0)
  Total = 0
  for x in range(len(First)):
    if First[x] == CurrentCave:
      if Second[x].islower():
        if Second[x] in Visited:
          if Twice == True:
            continue
          New = Visited.copy()
          New.append(Second[x])
          Total += Function(New, True)
          continue
      New = Visited.copy()
      New.append(Second[x])
      Total += (Function(New, Twice))
  return(Total)

print(Function(["start"], False))