"""
29: Distinct Powers
"""

Set = set([])
for a in range(2, 100 + 1):
    for b in range(2, 100 + 1):
        Set.add(a ** b)

print(len(Set))