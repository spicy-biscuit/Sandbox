Input = """1
3
5
11
13
17
19
23
29
31
37
41
43
47
53
59
67
71
73
79
83
89
97
101
103
107
109
113"""

from functools import cache

Input = Input.split()
for x in range(len(Input)):
    Input[x] = int(Input[x])

def FindGroupOfSize(RequiredTotal, RequiredAmount, Items):
    

def FindSmallestGroups(RequiredTotal, Items):
    GroupSize = 0
    while True:
        GroupSize += 1