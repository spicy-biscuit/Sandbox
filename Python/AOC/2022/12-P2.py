Input = ["""abaacccccccccccccaaaaaaaccccccccccccccccccccccccccccccccccaaaaaa
abaaccccccccccccccaaaaaaaaaaccccccccccccccccccccccccccccccccaaaa
abaaaaacccccccccaaaaaaaaaaaaccccccccccccccccccccccccccccccccaaaa
abaaaaaccccccccaaaaaaaaaaaaaacccccccccccccccccdcccccccccccccaaaa
abaaaccccccccccaaaaaaaaccacacccccccccccccccccdddcccccccccccaaaaa
abaaacccccccccaaaaaaaaaaccaaccccccccccccciiiiddddcccccccccccaccc
abcaaaccccccccaaaaaaaaaaaaaaccccccccccciiiiiijddddcccccccccccccc
abccaaccccccccaccaaaaaaaaaaaacccccccccciiiiiijjddddccccaaccccccc
abccccccccccccccaaacaaaaaaaaaaccccccciiiiippijjjddddccaaaccccccc
abccccccccccccccaacccccaaaaaaacccccciiiippppppjjjdddddaaaaaacccc
abccccccccccccccccccccaaaaaaccccccckiiippppppqqjjjdddeeeaaaacccc
abccccccccccccccccccccaaaaaaccccckkkiippppuupqqjjjjdeeeeeaaccccc
abccccccccccccccccccccccccaaccckkkkkkipppuuuuqqqjjjjjeeeeeaccccc
abccccccccccccccccccccccccccckkkkkkoppppuuuuuvqqqjjjjjkeeeeccccc
abcccccccccccccccccccccccccckkkkooooppppuuxuvvqqqqqqjkkkeeeecccc
abccaaccaccccccccccccccccccckkkoooooopuuuuxyvvvqqqqqqkkkkeeecccc
abccaaaaacccccaaccccccccccckkkoooouuuuuuuxxyyvvvvqqqqqkkkkeecccc
abcaaaaacccccaaaacccccccccckkkooouuuuxxxuxxyyvvvvvvvqqqkkkeeeccc
abcaaaaaaaaaaaaacccccccccccjjjooottuxxxxxxxyyyyyvvvvrrrkkkeecccc
abcccaaaacaaaaaaaaacaaccccccjjoootttxxxxxxxyyyyyyvvvrrkkkfffcccc
SbccaacccccaaaaaaaaaaaccccccjjjooottxxxxEzzzyyyyvvvrrrkkkfffcccc
abcccccccccaaaaaaaaaaaccccccjjjooootttxxxyyyyyvvvvrrrkkkfffccccc
abcaacccccaaaaaaaaaaaccccccccjjjooottttxxyyyyywwvrrrrkkkfffccccc
abaaacccccaaaaaaaaaaaaaacccccjjjjonnttxxyyyyyywwwrrlllkfffcccccc
abaaaaaaaaaaacaaaaaaaaaaccccccjjjnnnttxxyywwyyywwrrlllffffcccccc
abaaaaaaaaaaaaaaaaaaaaaaccccccjjjnntttxxwwwwwywwwrrlllfffccccccc
abaaccaaaaaaaaaaaaaaacccccccccjjjnntttxwwwsswwwwwrrlllfffccccccc
abaacccaaaaaaaacccaaacccccccccjjinnttttwwsssswwwsrrlllgffacccccc
abccccaaaaaaccccccaaaccccccccciiinnntttsssssssssssrlllggaacccccc
abccccaaaaaaaccccccccccaaccccciiinnntttsssmmssssssrlllggaacccccc
abccccaacaaaacccccccaacaaaccccciinnnnnnmmmmmmmsssslllgggaaaacccc
abccccccccaaacccccccaaaaacccccciiinnnnnmmmmmmmmmmllllgggaaaacccc
abaaaccccccccccccccccaaaaaacccciiiinnnmmmhhhmmmmmlllgggaaaaccccc
abaaaaacccccccccccaaaaaaaaaccccciiiiiiihhhhhhhhmmlgggggaaacccccc
abaaaaaccccaaccccaaaaaaacaacccccciiiiihhhhhhhhhhggggggcaaacccccc
abaaaaccccaaaccccaaaacaaaaacccccccciiihhaaaaahhhhggggccccccccccc
abaaaaaaacaaacccccaaaaaaaaaccccccccccccccaaaacccccccccccccccccaa
abaacaaaaaaaaaaaccaaaaaaaaccccccccccccccccaaaccccccccccccccccaaa
abcccccaaaaaaaaacccaaaaaaaccccccccccccccccaacccccccccccccccccaaa
abccccccaaaaaaaaaaaaaaaaacccccccccccccccccaaacccccccccccccaaaaaa
abcccccaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccaaaaaa"""]

# Input = ["""Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi"""]

Input = Input[0].split("\n")

Height = len(Input)
Width = len(Input[0])

MinDistanceGrid = [[float('inf') for x in range(Width)] for y in range(Height)]
Grid = [[0 for x in range(Width)] for y in range(Height)]

StartRow = 0
StartColumn = 0

EndRow = 0
EndColumn = 0

for Row in range(Height):
  for Column in range(Width):
    This = Input[Row][Column]
    if This == "S" or This == "a":
      StartRow = Row
      StartColumn = Column
      This = "a"
      MinDistanceGrid[StartRow][StartColumn] = 0
    if This == "E":
      EndRow = Row
      EndColumn = Column
      This = "z"
    Grid[Row][Column] = ord(This) - 96

MinDistanceGrid[StartRow][StartColumn] = 0

while True:
  Changes = 0
  for Row in range(Height):
    for Column in range(Width):
      This = Grid[Row][Column] - 1
      Old = MinDistanceGrid[Row][Column]
      List = [MinDistanceGrid[Row][Column]]
      if Row > 0:
        Other = Grid[Row - 1][Column]
        if Other >= This:
          List.append(MinDistanceGrid[Row - 1][Column] + 1)
      if Row < Height - 1:
        Other = Grid[Row + 1][Column]
        if Other >= This:
          List.append(MinDistanceGrid[Row + 1][Column] + 1)
      if Column > 0:
        Other = Grid[Row][Column - 1]
        if Other >= This:
          List.append(MinDistanceGrid[Row][Column - 1] + 1)
      if Column < Width - 1:
        Other = Grid[Row][Column + 1]
        if Other >= This:
          List.append(MinDistanceGrid[Row][Column + 1] + 1)
      MinDistanceGrid[Row][Column] = min(List)
      if Old != MinDistanceGrid[Row][Column]:
        Changes += 1
  # print("-----------------")
  # print(Changes)
  # for x in MinDistanceGrid:
  #   print(x)
  # print()
  # for x in Grid:
  #   print(x)
  # print("-----------------")
  if Changes == 0:
    break

print(MinDistanceGrid[EndRow][EndColumn])


#START FROM END
#GO EVERYWHERE
#FIND SMALLEST NUMBER
#THAT IS AN 'A'