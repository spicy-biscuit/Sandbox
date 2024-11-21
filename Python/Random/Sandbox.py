import math

String = ""
for x in range(1, 300000):
  if x % 1000 == 0:
    print(x)
  String = String + str(x)

print(String[0])
print(String[9])
print(String[99])
print(String[999])
print(String[9999])
print(String[99999])
print(String[999999])