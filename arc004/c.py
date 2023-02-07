import math

N = int(input())
xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

res = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a = xy[i]
        b = xy[j]
        l = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        if l > res:
            res = l

print(res)
