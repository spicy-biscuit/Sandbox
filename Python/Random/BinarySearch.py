import random
import timeit
import math

print("Please input your list of numbers, seperated by spaces.")
Input = input("")

if Input.count(" ") == 0:
  # Input = [random.randint(1, int(Input)**2) for x in range(int(Input))]
  Input = [random.randint(1,100) for x in range(int(Input))]
else:
  Input = Input.split()

for x in range(len(Input)):
  Input[x] = int(Input[x])

def RadixSort(Input):
  MaxLength = 0
  for x in range(len(Input)):
    Input[x] = str(Input[x])
    if len(Input[x]) > MaxLength:
      MaxLength = len(Input[x])
  for DIGIT in range(1, MaxLength+1):
    Buckets = [[] for x in range(10)]
    for NUMBER in Input:
      if len(NUMBER) < DIGIT:
        Buckets[0].append(NUMBER)
      else:
        Buckets[int(NUMBER[(-1)*DIGIT])].append(NUMBER)
    Input = []
    for x in Buckets:
      Input = Input + x
  return(Input)

Input = RadixSort(Input)

print(List)