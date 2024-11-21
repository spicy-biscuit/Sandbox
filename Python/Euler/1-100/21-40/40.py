"""
40: Champernowne's Constant
"""

x = 0
String = ""
Length = 0

while True:
    y = str(x)
    String = String + y
    Length += len(y)
    x += 1
    if Length > 1000000 + 100:
        break

# print(String)
print(int(String[1]) * int(String[10]) * int(String[100]) * int(String[1000]) * int(String[10000]) * int(String[100000]) * int(String[1000000]))