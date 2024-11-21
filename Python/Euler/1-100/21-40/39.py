"""
39: Integer Right Triangles
"""

Max = 0
Out = 0
for p in range(1, 1001):
    
    Solutions = 0
    for a in range(1, p):
        for b in range(a, p - a):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                Solutions += 1
    # print(p, Solutions)
    if Solutions > Max:
        Max = Solutions
        Out = p

print(Out, Max)
