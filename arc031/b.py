A = [list(input()) for _ in range(10)]
cnt = 0
areas = 0
for a in A:
    areas += a.count('o')


def dfs(x, y):
    global cnt

    if x < 0 or x >= 10 or y < 0 or y >= 10 or A[x][y] == 'x':
        return
    if r[x][y]:
        return

    r[x][y] = True
    cnt += 1

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


r = []
for i in range(10):
    for j in range(10):
        if A[i][j] == 'o':
            continue

        A[i][j] = 'o'
        r = [[False for _ in range(10)] for _ in range(10)]
        dfs(i, j)

        if cnt == areas + 1:
            print('YES')
            exit(0)
        A[i][j] = 'x'

        cnt = 0


print('NO')
