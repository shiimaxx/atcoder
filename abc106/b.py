N = int(input())
res = 0
for i in range(1, N+1):
    cnt = 0
    if i % 2 == 0:
        continue
    for j in range(i, 0, -1):
        if i % j == 0:
            cnt += 1
    if cnt == 8:
        res += 1

print(res)
