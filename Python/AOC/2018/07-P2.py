Input = ["""Step Q must be finished before step O can begin.
Step Z must be finished before step G can begin.
Step W must be finished before step V can begin.
Step C must be finished before step X can begin.
Step O must be finished before step E can begin.
Step K must be finished before step N can begin.
Step P must be finished before step I can begin.
Step X must be finished before step D can begin.
Step N must be finished before step E can begin.
Step F must be finished before step A can begin.
Step U must be finished before step Y can begin.
Step M must be finished before step H can begin.
Step J must be finished before step B can begin.
Step B must be finished before step E can begin.
Step S must be finished before step L can begin.
Step A must be finished before step L can begin.
Step E must be finished before step L can begin.
Step L must be finished before step G can begin.
Step D must be finished before step I can begin.
Step Y must be finished before step I can begin.
Step I must be finished before step G can begin.
Step G must be finished before step R can begin.
Step V must be finished before step T can begin.
Step R must be finished before step H can begin.
Step H must be finished before step T can begin.
Step S must be finished before step E can begin.
Step C must be finished before step E can begin.
Step P must be finished before step T can begin.
Step I must be finished before step H can begin.
Step O must be finished before step P can begin.
Step M must be finished before step L can begin.
Step S must be finished before step D can begin.
Step P must be finished before step D can begin.
Step P must be finished before step R can begin.
Step I must be finished before step R can begin.
Step Y must be finished before step G can begin.
Step Q must be finished before step L can begin.
Step N must be finished before step R can begin.
Step J must be finished before step E can begin.
Step N must be finished before step T can begin.
Step B must be finished before step V can begin.
Step Q must be finished before step B can begin.
Step J must be finished before step H can begin.
Step F must be finished before step B can begin.
Step W must be finished before step X can begin.
Step S must be finished before step T can begin.
Step J must be finished before step G can begin.
Step O must be finished before step R can begin.
Step K must be finished before step B can begin.
Step Z must be finished before step O can begin.
Step Q must be finished before step S can begin.
Step K must be finished before step V can begin.
Step B must be finished before step R can begin.
Step J must be finished before step T can begin.
Step E must be finished before step T can begin.
Step G must be finished before step V can begin.
Step D must be finished before step Y can begin.
Step M must be finished before step Y can begin.
Step F must be finished before step G can begin.
Step C must be finished before step P can begin.
Step V must be finished before step R can begin.
Step R must be finished before step T can begin.
Step J must be finished before step Y can begin.
Step U must be finished before step R can begin.
Step Z must be finished before step F can begin.
Step Q must be finished before step V can begin.
Step U must be finished before step M can begin.
Step J must be finished before step R can begin.
Step L must be finished before step V can begin.
Step W must be finished before step K can begin.
Step B must be finished before step Y can begin.
Step O must be finished before step N can begin.
Step D must be finished before step V can begin.
Step P must be finished before step B can begin.
Step U must be finished before step I can begin.
Step O must be finished before step T can begin.
Step S must be finished before step G can begin.
Step X must be finished before step A can begin.
Step U must be finished before step T can begin.
Step A must be finished before step I can begin.
Step B must be finished before step G can begin.
Step N must be finished before step Y can begin.
Step Z must be finished before step J can begin.
Step M must be finished before step D can begin.
Step U must be finished before step A can begin.
Step S must be finished before step R can begin.
Step Z must be finished before step A can begin.
Step Y must be finished before step R can begin.
Step E must be finished before step Y can begin.
Step N must be finished before step G can begin.
Step Z must be finished before step X can begin.
Step P must be finished before step X can begin.
Step Z must be finished before step T can begin.
Step Z must be finished before step P can begin.
Step V must be finished before step H can begin.
Step P must be finished before step L can begin.
Step L must be finished before step H can begin.
Step X must be finished before step V can begin.
Step W must be finished before step G can begin.
Step N must be finished before step D can begin.
Step Z must be finished before step U can begin."""]

# Input = ["""Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""]

Input = Input[0].split("\n")

Instructions = []

Remaining = [chr(x + 65) for x in range(26)]
Finished = []

for x in Input:
  Requirement = x[5]
  ToDo = x[36]
  Instructions.append((ToDo, Requirement))

def CheckValid(Step, Done, Instruction):
  for x in Instruction:
    if x[0] == Step:
      if x[1] not in Done:
        return(False)
  return(True)

print(Instructions)

Steps = [1000 for x in range(26)]


Completed = []

print(Steps)
    
CurrentlyWorking = [False for x in range(26)]
WorkingNum = 0

Seconds = 0
while True:
  Seconds += 1
  print(Seconds, WorkingNum, Completed)
  for x in range(len(CurrentlyWorking)):
    if CurrentlyWorking[x]:
      Steps[x] -= 1
      if Steps[x] == 0:
        CurrentlyWorking[x] = False
        Completed.append(chr(x + 65))
        WorkingNum -= 1

  for x in range(26):
    Letter = chr(x + 65)
    if Letter in Completed:
      continue
    if CurrentlyWorking[x]:
      continue
    if WorkingNum > 4:
      break
    if CheckValid(Letter, Completed, Instructions):
      WorkingNum += 1
      Steps[x] = x + 61
      CurrentlyWorking[x] = True
      continue
  if len(Completed) == 26:
    break
print(Seconds - 1)