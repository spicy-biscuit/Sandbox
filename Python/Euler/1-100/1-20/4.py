"""
4: Largest Palindrome Product
"""

List = set([])

for a in range(1, 1000):
  for b in range(1, 1000):
    List.add(a * b)

List = list(List)
List.sort(reverse=True)

def IsPalindrome(N):
  N = str(N)
  if N == N[::-1]:
    return(True)
  return(False)

for x in List:
  if IsPalindrome(x):
    print(x)
    break