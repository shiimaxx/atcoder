H, W = map(int, input().split())
h, w = H - 1, W - 1
s = [list(input()) for _ in range(H)]
d = [[-1 for _ in range(W)] for _ in range(H)]

num_whites = 0
for si in s:
    for sj in si:
        if sj == '.':
            num_whites += 1

q = [[0, 0]]
d[0][0] = 0

while len(q) > 0:
    i, j = q.pop(0)

    for n in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        ni, nj = n[0], n[1]
        if ni < 0 or ni >= H or nj < 0 or nj >= W or s[ni][nj] == '#' or d[ni][nj] != -1:
            continue
        d[ni][nj] = d[i][j] + 1
        q.append([ni, nj])

print(num_whites - (d[h][w] + 1)) if d[h][w] != -1 else print(-1)
