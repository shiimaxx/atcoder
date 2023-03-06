from collections import deque

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
si, sj, gi, gj = -1, -1, -1, -1
for i in range(H):
    for j in range(W):
        if c[i][j] == 's':
            si, sj = i, j
        if c[i][j] == 'g':
            gi, gj = i, j

d = [[-1 for _ in range(W)] for _ in range(H)]
d[si][sj] = 0
q = deque([[si, sj]])

while len(q) > 0:
    i, j = q.popleft()

    for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if ni < 0 or ni >= H or nj < 0 or nj >= W or d[ni][nj] != -1:
            continue

        if c[ni][nj] == '.':
            d[ni][nj] = d[i][j]
            q.insert(0, [ni, nj])
        elif c[ni][nj] == '#':
            d[ni][nj] = d[i][j] + 1
            q.append([ni, nj])
        else:
            d[ni][nj] = d[i][j]

print('YES') if d[gi][gj] <= 2 else print('NO')
