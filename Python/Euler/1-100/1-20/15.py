"""
15: Lattice Paths
"""

Size = 20

# Size choose 2 * Size

Big = 2 * Size
Out = 1
for x in range(Size):
  Out *= Big
  Big -= 1

for x in range(1, Size + 1):
  Out //= x

print(Out)