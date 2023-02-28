R, C = map(int, input().split())
sy, sx = map(int, input().split())
sy, sx = sy-1, sx-1
gy, gx = map(int, input().split())
gy, gx = gy-1, gx-1
c = [list(input()) for _ in range(R)]
d = [[-1 for _ in range(C)] for _ in range(R)]

cnt = 0
queue = [[sy, sx]]
d[sy][sx] = 0
while len(queue) > 0:
    y, x = queue.pop(0)

    for n in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
        ny, nx = n[0], n[1]
        if ny < 0 or ny >= R or nx < 0 or nx >= C or c[ny][nx] == '#' or d[ny][nx] != -1:
            continue

        d[ny][nx] = d[y][x] + 1
        queue.append([ny, nx])

print(d[gy][gx])
