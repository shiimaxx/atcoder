N, M = map(int, input().split())
a = [[] for _ in range(N)]
for _ in range(M):
    ai, bi = map(int, input().split())
    ai, bi = ai - 1, bi - 1
    a[ai].append(bi)
    a[bi].append(ai)
cnt = 0


def search(x):
    global cnt
    # print(f"search({x}): {visited}")

    if False not in visited:
        cnt += 1
        return

    for ax in a[x]:
        if visited[ax]:
            continue
        visited[ax] = True
        search(ax)
        visited[ax] = False


visited = []
for ai in a[0]:
    visited = [False for _ in range(N)]
    visited[0] = True
    visited[ai] = True
    search(ai)

print(cnt)
