import math

A, B, C, X, Y = map(int, input().split())

min = 0
XY = X * 2 if X > Y else Y * 2
for xy in range(XY+1):
    x = math.ceil(X - (xy / 2)) if X > (xy / 2) else 0
    y = math.ceil(Y - (xy / 2)) if Y > (xy / 2) else 0
    total = int((A * x) + (B * y) + (C * xy))
    if min == 0 or total < min:
        min = total

print(min)
