"""
63: Powerful Digit Counts
"""

Count = 0
for Power in range(1, 101):
    for Base in range(1, 11):
        Number = Base ** Power
        Number = str(Number)
        if len(Number) == Power:
            Count += 1
print(Count)
