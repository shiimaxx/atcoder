H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        cnt = 0
        cnt = cnt + 1 if j < W-1 and S[i][j+1] == '#' else cnt
        cnt = cnt + 1 if j > 0 and S[i][j-1] == '#' else cnt
        cnt = cnt + 1 if i < H-1 and S[i+1][j] == '#' else cnt
        cnt = cnt + 1 if i < H-1 and j < W-1 and S[i+1][j+1] == '#' else cnt
        cnt = cnt + 1 if i < H-1 and j > 0 and S[i+1][j-1] == '#' else cnt
        cnt = cnt + 1 if i > 0 and S[i-1][j] == '#' else cnt
        cnt = cnt + 1 if i > 0 and j < W-1 and S[i-1][j+1] == '#' else cnt
        cnt = cnt + 1 if i > 0 and j > 0 and S[i-1][j-1] == '#' else cnt
        S[i][j] = str(cnt)

for s in S:
    print(''.join(s))
