H, W, N = map(int, input().split())
s = [list(input()) for _ in range(H)]
d = [[-1 for _ in range(W)] for _ in range(H)]

start = None
for i, si in enumerate(s):
    start = [i, si.index('S')] if 'S' in si else None
    if start:
        break

q = [start]
d[start[0]][start[1]] = 0
end = None

while len(q) > 0:
    i, j = q.pop(0)

    for n in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        ni, nj = n[0], n[1]
        if ni < 0 or ni >= H or nj < 0 or nj >= W or s[ni][nj] == 'X' or d[ni][nj] != -1:
            continue
        d[ni][nj] = d[i][j] + 1
        q.append([ni, nj])
        if s[ni][nj] == '1':
            end = [ni, nj]
            break

i, j = end
print(d[i][j])
