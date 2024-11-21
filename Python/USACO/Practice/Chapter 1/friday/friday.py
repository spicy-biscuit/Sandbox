'''
ID: ethanfung8
LANG: PYTHON3
PROG: friday
'''

# File = open(r"USACO/Practice/Chapter 1/friday/friday.in", "r")
File = open(r"friday.in", "r")
Input = File.read()
File.close()

N = int(Input)

ThirtyDays = [4, 6, 9, 11]
ThirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
DayOfWeek = 2
Day = 0
Month = 1
Year = 1900

def IsLeapYear():
  if Year % 400 == 0:
    return(True)
  if Year % 100 == 0:
    return(False)
  if Year % 4 == 0:
    return(True)
  return(False)

Thirteenths = [0 for x in range(7)]

while Year < 1900 + N:
  Day += 1
  DayOfWeek += 1
  if DayOfWeek == 8:
    DayOfWeek = 1
  if Day > 31:
    Month += 1
    Day = 1
  elif Day > 30 and Month in ThirtyDays:
    Month += 1
    Day = 1
  elif Day > 29 and Month == 2 and IsLeapYear():
    Month += 1
    Day = 1
  elif Day > 28 and Month == 2 and not IsLeapYear():
    Month += 1
    Day = 1
  if Month > 12:
    Month = 1
    Year += 1

  if Day == 13:
    Thirteenths[DayOfWeek - 1] = Thirteenths[DayOfWeek - 1] + 1

# File = open(r"USACO/Practice/Chapter 1/friday/friday.out", "x")
File = open(r"friday.out", "x")
for x in range(7):
  if x != 6:
    File.write(str(Thirteenths[x]) + " ")
  else:
    File.write(str(Thirteenths[x]) + "\n")
File.close()