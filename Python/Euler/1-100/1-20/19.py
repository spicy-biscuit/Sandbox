"""
19: Counting Sundays
"""

def IsLeapYear(N):
  if N % 400 == 0:
    return(True)
  if N % 100 == 0:
    return(False)
  if N % 4 == 0:
    return(True)
  return(False)

Day = 0
#1 is sunday, 2 is monday...
DayOfWeek = 0
Month = 1
Year = 1901

Out = 0

while True:
  Day += 1
  DayOfWeek += 1

  if DayOfWeek == 8:
    DayOfWeek = 1

  #31 days
  if Month in [1, 3, 5, 7, 8, 10, 12]:
    if Day == 32:
      Day = 1
      Month += 1

  #30 days
  if Month in [4, 6, 9, 11]:
    if Day == 31:
      Day = 1
      Month += 1

  #February
  if Month == 2:
    if Day == 29 and not IsLeapYear(Year):
      Day = 1
      Month += 1
    if Day == 30 and IsLeapYear(Year):
      Day = 1
      Month += 1

  #Increment year
  if Month == 13:
    Month = 1
    Year += 1

  if Year == 2001:
    break

  if Day == 1 and DayOfWeek == 1:
    Out += 1
    

print(Out)