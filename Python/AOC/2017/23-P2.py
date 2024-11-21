Input = ["""
set b 79
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""]

c = 124900

def Min(a, b):
  List = []
  if a > 0:
    List.append(a)
  if b > 0:
    List.append(b)
  return(min(List))

Output = 0
for b in reversed(range(1001)):
  # print(b)
  b = c - 17 * b
  # print(b)
  f = 1
  d = 2
  e = 2
  Breakout = False
  while True:
    # print(d)
    e = 2
    while True:
      if d * e == b:
        f = 0
        print((c - b)/17, d)
        Breakout = True
        break
      if d != 0 and ((b / d) % 1 > 0.99999 or (b / d) % 1 < 0.00001):
        e += Min(int(b / d) - e, b - e)
      else:
        e = b
      if e == b:
        break
    if Breakout:
      break
    d += 1
    # if d < 50000:
    #   d = 50000
    if b == d:
      break
      
  if f == 0:
    Output += 1
    # print('f')
  if b == c:
    break

print(Output)
      