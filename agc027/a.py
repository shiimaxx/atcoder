N, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

res = 0
for i, ai in enumerate(a):
    x -= ai
    res += 1
    if x < 1:
        break

if x != 0:
    res -= 1

print(res)
