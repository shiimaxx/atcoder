N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
ab.sort(key=lambda x: x[1])

cnt = 0
last = -1
for a, b in ab:
    if last <= a:
        cnt += 1
        last = b

print(cnt)
