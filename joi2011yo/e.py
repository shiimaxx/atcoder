H, W, N = map(int, input().split())
s = [list(input()) for _ in range(H)]
d = [[-1 for _ in range(W)] for _ in range(H)]

start = None
Si, Sj = -1, -1
for i, si in enumerate(s):
    Si, Sj = [i, si.index('S')] if 'S' in si else [Si, Sj]

visited = []
q = [[Si, Sj]]
d[Si][Sj] = 0
total = 0
HP = 1

while len(q) > 0:
    i, j = q.pop(0)
    if s[i][j].isdigit() and HP >= int(s[i][j]) and s[i][j] not in visited:
        HP += 1
        total += d[i][j]
        visited.append(s[i][j])
        d = [[-1 for _ in range(W)] for _ in range(H)]
        d[i][j] = 0
        q = [[i, j]]
        continue

    for n in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        ni, nj = n[0], n[1]
        if ni < 0 or ni >= H or nj < 0 or nj >= W or s[ni][nj] == 'X' or d[ni][nj] != -1:
            continue
        d[ni][nj] = d[i][j] + 1
        q.append([ni, nj])

print(total)
