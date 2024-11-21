Input = ["""33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42"""]

Input = Input[0].split()
for x in range(len(Input)):
  Input[x] = int(Input[x])
Input = tuple(Input)
print(Input)

from functools import cache

@cache
def Function(N, List):
  List = list(List)
  if N == 0:
    return(1)
  if N < 0:
    return(0)
  if len(List) == 0:
    return(0)
  FirstItem = List[0]
  Tuple = tuple(List[1:])
  return(Function(N - FirstItem, Tuple) + Function(N, Tuple))

print(Function(25, (5, 5, 10, 15, 20)))
print(Function(150, Input))
