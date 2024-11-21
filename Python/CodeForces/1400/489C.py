"""
489C: Given Length and Sum of Digits...
"""

Line1 = input()
Line1 = list(map(int, Line1.split()))

# print(Line1)

Length = Line1[0]
Sum = Line1[1]

if Length == 1 and Sum == 0:
  print("0 0")

elif Sum > Length * 9 or Sum == 0:
  print("-1 -1")

else:
  Out = ""
  if Sum > (Length - 1) * 9:
    #If first digit is not a 1
    Number = ["0" for x in range(Length)]
    Index = Length
    while True:
      if Sum == 0:
        break
      Index -= 1
      if Sum >= 9:
        Sum -= 9
        Number[Index] = "9"
      else:
        Number[Index] = str(Sum)
        Sum = 0
    
  else:
    #First digit is a 1
    Number = ["0" for x in range(Length)]
    Number[0] = "1"
    Sum -= 1
    Index = Length
    while True:
      if Sum == 0:
        break
      Index -= 1
      if Sum >= 9:
        Sum -= 9
        Number[Index] = "9"
      else:
        Number[Index] = str(Sum)
        Sum = 0
    # print(Number)

  for x in Number:
    Out = Out + x
  Out = Out + " "

  #Max num now
  Sum = Line1[1]
  Number = ["0" for x in range(Length)]
  Index = -1
  while True:
    Index += 1
    if Sum == 0:
      break
    if Sum >= 9:
      Number[Index] = "9"
      Sum -= 9
    else:
      Number[Index] = str(Sum)
      Sum = 0
  
  for x in Number:
    Out = Out + x
  Out = Out

  print(Out)

"""
ACCEPTED!
"""