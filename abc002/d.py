N, M = map(int, input().split())
relations = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    relations[x-1][y-1] = 1
    relations[y-1][x-1] = 1

max_members = 1
for n in range(2 ** N):
    ok = True
    for i in range(N):
        for j in range(i):
            if ((n >> i) & 1) and ((n >> j) & 1) and relations[i][j] == 0:
                ok = False
    if ok:
        max_members = max(max_members, bin(n).count("1"))

print(max_members)
