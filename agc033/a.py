from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            q.append([i, j, 0])

cnt = 0
while len(q) > 0:
    i, j, cnt = q.popleft()
    for n in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        ni, nj = n[0], n[1]
        if ni < 0 or ni >= H or nj < 0 or nj >= W or A[ni][nj] == '#':
            continue
        A[ni][nj] = '#'
        q.append([ni, nj, cnt+1])

print(cnt)
