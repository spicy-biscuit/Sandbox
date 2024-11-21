import random
import timeit
import math
import os

os.system("clear")

print("Please input your list of numbers, seperated by spaces.")
Input = input("")

if Input.count(" ") == 0:
  Input = [random.randint(1, int(Input)**2) for x in range(int(Input))]
else:
  Input = Input.split()

for x in range(len(Input)):
  Input[x] = int(Input[x])

if len(Input) < 10001:
  print("\nBefore Sort:")
  print(Input)
  
print("\nPlease select a sorting method:\n'0' - All sorting methods, with times listed\n'1' - Bubble Sort\n'2' - Insertion Sort\n'3' - Selection Sort\n'4' - Merge Sort\n'5' - Counting Sort\n'6' - Radix Sort\n'7' - Quick Sort\n'8' - Stalin Sort")
SortingType = input("Selection Choice: ").split()

for x in range(len(SortingType)):
  SortingType[x] = int(SortingType[x])

#Bubble Sort
def BubbleSort(Input):
  for Counter in range(0, len(Input)):
    for Pointer in range(0, len(Input)-1):
      Value1 = Input[Pointer]
      Value2 = Input[Pointer+1]
      if Value2 < Value1:
        Input[Pointer] = Value2
        Input[Pointer+1] = Value1
  return(Input)

#Insertion Sort
def InsertionSort(Input):
  def Insert(List, Number):
    if List == []:
      return([Number])
    for Pointer in range(len(List)):
      if List[Pointer] >= Number:
        List.insert(Pointer, Number)
        return(List)
    return(List + [Number])
  for x in range(1, len(Input)):
    Input = Insert(Input[:x], Input[x]) + Input[x+1:]
  return(Input)

#SelectionSort
def SelectionSort(Input):
  def IndexOfMin(List):
    Min = List[0]
    Output = 0
    for y in range(len(List)):
      if List[y] < Min:
        Min = List[y]
        Output = y
    return(Output)
  for x in range(len(Input)):
    Mini = IndexOfMin(Input[x:])
    Input[x], Input[Mini+x] = Input[Mini+x], Input[x]
  return(Input)

#MergeSort
def MergeSort(Input):
  if len(Input) == 1:
    return(Input)
  Length = len(Input)
  Length = math.ceil(Length/2)
  List1 = MergeSort(Input[:Length])
  List2 = MergeSort(Input[Length:])
  Input = []
  while List1 != [] and List2 != []:
    if List1[0] < List2[0]:
      Input.append(List1[0])
      List1 = List1[1:]
    else:
      Input.append(List2[0])
      List2 = List2[1:]
  return(Input + List1 + List2)

#Counting Sort
def CountingSort(Input):
  Maximum = Input[0]
  Minimum = Input[0]
  for x in Input:
    if x < Minimum:
      Minimum = x
    if x > Maximum:
      Maximum = x
  CountingList = [0 for x in range(Maximum-Minimum+1)]
  for x in Input:
    CountingList[x-Minimum] = CountingList[x-Minimum]+1
  Input = []
  for x in range(len(CountingList)):
    for y in range(CountingList[x]):
      Input.append(x+Minimum)
  return(Input)

#Radix Sort
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

#QuickSort
def QuickSort(Input):
  if len(Input) == 1:
    return(Input)
  Pivot = Input[0]
  LowerList = []
  UpperList = []
  for x in Input[1:]:
    if x > Pivot:
      UpperList.append(x)
    else:
      LowerList.append(x)
  return(LowerList + [Pivot] + UpperList)

#StalinSort
def StalinSort(Input):
  newList = []
  lastNum = Input[0]
  for i in range(len(Input)):
    if Input[i] >= lastNum:
      lastNum = Input[i]
      newList.append(lastNum)
  return(newList)

FullSorted = Input
String = ""
Start = timeit.default_timer()
if 0 in SortingType or 1 in SortingType:
  StartBubble = timeit.default_timer()
  BubbleSorted = BubbleSort(Input)
  EndBubble = timeit.default_timer()
  String = String + "\nBubble Sort:    " + str(EndBubble - StartBubble) + " seconds"
  FullSorted = BubbleSorted
if 0 in SortingType or 2 in SortingType:
  StartInsertion = timeit.default_timer()
  InsertionSorted = InsertionSort(Input)
  EndInsertion = timeit.default_timer()
  String = String + "\nInsertion Sort: " + str(EndInsertion - StartInsertion) + " seconds"
  FullSorted = InsertionSorted
if 0 in SortingType or 3 in SortingType:
  StartSelection = timeit.default_timer()
  SelectionSorted = SelectionSort(Input)
  EndSelection = timeit.default_timer()
  String = String + "\nSelection Sort: " + str(EndSelection - StartSelection) + " seconds"
  FullSorted = SelectionSorted
if 0 in SortingType or 4 in SortingType:
  StartMerge = timeit.default_timer()
  MergeSorted = MergeSort(Input)
  EndMerge = timeit.default_timer()
  String = String + "\nMerge Sort:     " + str(EndMerge - StartMerge) + " seconds"
  FullSorted = MergeSorted
if 0 in SortingType or 5 in SortingType:
  StartCounting = timeit.default_timer()
  CountingSorted = CountingSort(Input)
  EndCounting = timeit.default_timer()
  String = String + "\nCounting Sort:  " + str(EndCounting - StartCounting) + " seconds"
  FullSorted = CountingSorted
if 0 in SortingType or 6 in SortingType:
  StartRadix = timeit.default_timer()
  RadixSorted = RadixSort(Input)
  EndRadix = timeit.default_timer()
  String = String + "\nRadix Sort:     " + str(EndRadix - StartRadix) + " seconds"
  FullSorted = RadixSorted
if 0 in SortingType or 7 in SortingType:
  StartQuick = timeit.default_timer()
  QuickSorted = QuickSort(Input)
  EndQuick = timeit.default_timer()
  String = String + "\nQuick Sort:     " + str(EndQuick - StartQuick) + " seconds"
  FullSorted = QuickSorted
if 0 in SortingType or 8 in SortingType:
  StartStalin = timeit.default_timer()
  StalinSorted = StalinSort(Input)
  EndStalin = timeit.default_timer()
  String = String + "\nStalin Sort:     " + str(EndStalin - StartStalin) + " seconds"
  FullSorted = StalinSorted

if len(FullSorted) < 10001:
  print("\nAfter Sort:")
  print(FullSorted)
print(String)