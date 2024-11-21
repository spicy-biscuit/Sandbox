Input = ["""2238518614
4552388553
2562121143
2666685337
7575518784
3572534871
8411718283
7742668385
1235133231
2546165345"""]

# Input = ["""5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""]

Input = Input[0].split("\n")

Height = len(Input)
Width = len(Input[0])

for x in range(Height):
  Input[x] = list(Input[x])

for Row in range(Height):
  for Column in range(Width):
    Input[Row][Column] = int(Input[Row][Column])

# print(Input)

Flashes = 0
Step = 0
while True:
  Step += 1
  Flashes = 0
  Flashed = [[False for x in range(Width)] for x in range(Height)]

  for Row in range(Height):
    for Column in range(Width):
      Input[Row][Column] += 1
  
  while True:
    Break = True
    for Row in range(Height):
      for Column in range(Width):
        if Input[Row][Column] > 9 and Flashed[Row][Column] == False:
          #Flash!
          Flashes += 1
          Flashed[Row][Column] = True
          if Row > 0:
            Input[Row - 1][Column] += 1
          if Row < Height - 1:
            Input[Row + 1][Column] += 1
          if Column > 0:
            Input[Row][Column - 1] += 1
          if Column < Width - 1:
            Input[Row][Column + 1] += 1
          if Row > 0 and Column > 0:
            Input[Row - 1][Column - 1] += 1
          if Row > 0 and Column < Width - 1:
            Input[Row - 1][Column + 1] += 1
          if Row < Height - 1 and Column > 0:
            Input[Row + 1][Column - 1] += 1
          if Row < Height - 1 and Column < Width - 1:
            Input[Row + 1][Column + 1] += 1
          Break = False
    if Break:
      break

  if Flashes == Width * Height:
    print(Step)
    break
  for Row in range(Height):
    for Column in range(Width):
      if Input[Row][Column] > 9:
        Input[Row][Column] = 0

# print(Flashes)

  
        
