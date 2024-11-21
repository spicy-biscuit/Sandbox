"""
520B: Two Buttons
"""

Line1 = input()
Line1 = list(map(int, Line1.split()))

n = Line1[0]
m = Line1[1]

Options = set([n])

Seen = set([])

List = set([])

Cycle = 0
while True:
  # print(Cycle)
  Cycle += 1
  # print(Options)

  NewOptions = set([])

  for x in Options:
    if x in Seen:
      continue
    Seen.add(x)
    if x > m:
      List.add(x - m + Cycle - 1)
    else:
      if x > 1:
        NewOptions.add(x - 1)
      NewOptions.add(2 * x)

  Options.clear()
  Options = NewOptions
  # print(Options)
  if len(Options) == 0:
    ThisOut = float('inf')
    break
  if m in Options:
    ThisOut = Cycle
    break


if len(List) == 0:
  Out = float('inf')
else:
  Out = min(List)
Out = (min(Out, ThisOut))
print(Out)

"""
ACCEPTED!
"""