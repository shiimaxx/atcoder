N, M = map(int, input().split())
roads = [0 for i in range(N)]

for _ in range(M):
    ai, bi = map(int, input().split())
    roads[ai-1] += 1
    roads[bi-1] += 1

for r in roads:
    print(r)
