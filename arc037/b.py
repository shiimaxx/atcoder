N, M = map(int, input().split())
vertexes = [[] for _ in range(N+1)]
visited = []

for _ in range(M):
    u, v = map(int, input().split())
    vertexes[u].append(v)


def dfs(v, p):
    # print(v, p)
    if v in visited:
        return False

    visited.append(v)
    result = [dfs(y, v) for y in vertexes[v]]
    return False not in result


num_tree = 0
for i in range(1, N+1):
    if i in visited:
        continue
    if dfs(i, -1):
        num_tree += 1

print(num_tree)
