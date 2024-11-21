"""
1363B: Subsequence Hate
"""

def Min(List):
  A = List[0::2]
  B = List[1::2]
  return(min(sum(A), sum(B)))

T = int(input())

for Testcase in range(T):
  S = input()
  List = []
  Previous = S[0]
  Count = 0
  for x in range(len(S)):
    CurrentCharacter = S[x]
    if CurrentCharacter == Previous:
      Count += 1
      continue

    List.append(Count)
    Count = 0
    Previous = CurrentCharacter
    Count = 1
  List.append(Count)
  
  # print(List)

  MinVal = float('inf')
  for x in range(1, len(List)):
    First = List[:x]
    Second = List[x:]
    ThisVal = Min(First) + Min(Second)
    if ThisVal < MinVal:
      MinVal = ThisVal

  if MinVal == float('inf'):
    MinVal = 0
  print(MinVal)

"""
ACCEPTED!
"""