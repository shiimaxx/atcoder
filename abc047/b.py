W, H, N = map(int, input().split())
xy = [[0 for _ in range(H)] for _ in range(W)]

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for xx in range(x-1, -1, -1):
            for yy in range(0, H):
                xy[xx][yy] = 1
    elif a == 2:
        for xx in range(x, W):
            for yy in range(0, H):
                xy[xx][yy] = 1
    elif a == 3:
        for xx in range(0, W):
            for yy in range(y-1, -1, -1):
                xy[xx][yy] = 1
    elif a == 4:
        for xx in range(0, W):
            for yy in range(y, H):
                xy[xx][yy] = 1

cnt = 0
for x in xy:
    for y in x:
        if y == 0:
            cnt += 1

print(cnt)
