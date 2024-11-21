Input = ["""84
60
10
23
126
2
128
63
59
69
127
73
140
55
154
133
36
139
4
70
110
97
153
105
41
106
79
145
35
134
146
148
13
77
49
107
46
138
88
152
83
120
52
114
159
158
53
76
16
28
89
25
42
66
119
3
17
67
94
99
7
56
85
122
18
20
43
160
54
113
29
130
19
135
30
80
116
91
161
115
141
102
37
157
129
34
147
142
151
68
78
24
90
121
123
33
98
1
40"""]

# Input = ["""16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""]

Input = Input[0].split("\n")

for x in range(len(Input)):
  Input[x] = int(Input[x])

Input.sort()
# Input = [0] + Input
Input.append(Input[-1] + 3)

print(Input)
Input = tuple(Input)
from functools import cache

@cache
def Function(LastAdapter, Remaining):
  Total = 0
  if len(Remaining) == 0:
    return(1)
  for x in Remaining:
    if x - LastAdapter <= 3:
      New = Remaining[Remaining.index(x) + 1:]
      Total += Function(x, New)
  return(Total)

print(Function(0, tuple(Input)))
      