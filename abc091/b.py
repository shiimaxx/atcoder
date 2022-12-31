bucket = {}
N = int(input())

for _ in range(N):
    s = input()
    if s not in bucket:
        bucket[s] = 1
    else:
        bucket[s] += 1

M = int(input())
for _ in range(M):
    t = input()
    if t not in bucket:
        bucket[t] = -1
    else:
        bucket[t] -= 1

max = 0
for v in bucket.values():
    if v > max:
        max = v

print(max)
