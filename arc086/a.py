N, K = map(int, input().split())
A = map(int, input().split())

b = {}
for a in A:
    if a not in b:
        b[a] = 1
    else:
        b[a] += 1

sorted_b = sorted(b.items(), key=lambda x: x[1])

res = 0
for i, v in enumerate(sorted_b):
    if i + 1 > len(b) - K:
        break
    res += v[1]

print(res)
